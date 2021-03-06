from rest_framework import serializers
from .models import Workout, Lift, LiftEntry, Set, RunEntry

class WorkoutSerializer(serializers.ModelSerializer):

    class Meta:
        model = Workout
        fields = ('id', 'description', 'date', 'is_active')

class LiftSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lift
        fields = ('id', 'name', 'description', 'is_active')

class SetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Set
        fields = ('id', 'num_reps', 'weight', 'is_active')

class LiftEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = LiftEntry
        fields = ('id', 'lift', 'notes', 'is_active')

class RunEntrySerializer(serializers.ModelSerializer):

    class Meta:
        model = RunEntry
        fields = ('id', 'notes', 'distance', 'duration', 'elevation_delta', 'is_active')