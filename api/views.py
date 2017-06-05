from django.shortcuts import get_object_or_404
from rest_framework.generics import CreateAPIView,UpdateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework import status

from .models import Lift
from .serializers import LiftSerializer

# Workout Views

class CreateLiftView(CreateAPIView):
    serializer_class = LiftSerializer

    def perform_create(self,serializer):
        serializer.save(user=self.request.user)

class ListLiftsView(ListAPIView):
    serializer_class = LiftSerializer

    def get_queryset(self):
        return Lift.objects.filter(user=self.request.user)

class DetailLiftView(RetrieveAPIView):
    serializer_class = LiftSerializer
    queryset = Lift.objects.all()

class UpdateLiftView(UpdateAPIView):
    serializer_class = LiftSerializer
    queryset = Lift.objects.all()
