from rest_framework import serializers
from .models import Workout, Lift, LiftEntry, Set, RunEntry

class WorkoutSerializer(serializers.ModelSerializer):

    class Meta:
        model = Workout
        fields = ('id', 'description', 'date')

class LiftSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lift
        fields = ('id', 'name', 'description')

class SetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Set
        fields = ('id', 'set_num', 'num_reps', 'weight')

class LiftEntrySerializer(serializers.ModelSerializer):
    lift = LiftSerializer()

    class Meta:
        model = LiftEntry
        fields = ('id', 'lift', 'notes')

class RunEntrySerializer(serializers.ModelSerializer):

    class Meta:
        model = RunEntry
        fields = ('id', 'notes', 'distance', 'duration', 'elevation_delta')