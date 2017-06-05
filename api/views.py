import datetime
from django.shortcuts import get_object_or_404
from rest_framework.generics import CreateAPIView,UpdateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework import status

from .models import Lift, Set
from .permissions import LiftUserMatches, ParentLiftUserMatches
from .serializers import LiftSerializer, SetSerializer
# Workout Views

class CreateLiftView(CreateAPIView):
    permission_classes = (LiftUserMatches,)

    serializer_class = LiftSerializer

    def perform_create(self,serializer):
        serializer.save(user=self.request.user)

class ListLiftsView(ListAPIView):
    permission_classes = (LiftUserMatches,)

    serializer_class = LiftSerializer

    def get_queryset(self):
        return Lift.objects.filter(user=self.request.user)

class DetailLiftView(RetrieveAPIView):
    permission_classes = (LiftUserMatches,)

    serializer_class = LiftSerializer
    queryset = Lift.objects.all()

class UpdateLiftView(UpdateAPIView):
    permission_classes = (LiftUserMatches,)

    serializer_class = LiftSerializer
    queryset = Lift.objects.all()

# Lift Entry Views

class CreateSetView(CreateAPIView):
    permission_classes = (ParentLiftUserMatches,)
    serializer_class = SetSerializer

class ListSetsView(ListAPIView):
    permission_classes = (ParentLiftUserMatches,)
    serializer_class = SetSerializer

    def get_queryset(self):
        default_date = datetime.datetime.now().date()

        query_params = self.request.query_params
        start_date = query_params['start_date'] if 'start_date' in query_params else default_date
        end_date = query_params['end_date'] if 'end_date' in query_params else default_date

        filtered_sets = Set.objects.filter(entry_date__range=(start_date,start_date),lift__user=self.request.user)

        return filtered_sets

class DetailSetView(RetrieveAPIView):
    permission_classes = (ParentLiftUserMatches,)
    serializer_class = SetSerializer
    queryset = Set.objects.all()

class UpdateSetView(UpdateAPIView):
    permission_classes = (ParentLiftUserMatches,)
    serializer_class = SetSerializer
    queryset = Set.objects.all()

