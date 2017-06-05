from django.shortcuts import get_object_or_404
from rest_framework.generics import CreateAPIView,UpdateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework import status

from .models import Workout
from .serializers import WorkoutSerializer, LiftSerializer

# Workout Views

class CreateWorkoutView(CreateAPIView):
    serializer_class = WorkoutSerializer

    def perform_create(self,serializer):
        serializer.save(user=self.request.user)

class ListWorkoutsView(ListAPIView):
    serializer_class = WorkoutSerializer

    def get_queryset(self):
        return Workout.objects.filter(user=self.request.user)

class DetailWorkoutView(RetrieveAPIView):
    serializer_class = WorkoutSerializer
    queryset = Workout.objects.all()

class UpdateWorkoutView(UpdateAPIView):
    serializer_class = WorkoutSerializer
    queryset = Workout.objects.all()


# Lift Views

class CreateLiftView(CreateAPIView):
    serializer_class = LiftSerializer

    def perform_create(self,serializer):
        serializer.save(user=self.request.user)