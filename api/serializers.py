from rest_framework import serializers
from .models import Workout, Lift, LiftEntry, Set, Run, RunEntry


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


class RunSerializer(serializers.ModelSerializer):
    class Meta:
        model = Run
        fields = ('id', 'name', 'distance', 'elevation_delta')


class RunEntrySerializer(serializers.ModelSerializer):
    run = RunSerializer(read_only=True)
    run_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = RunEntry
        fields = ('id', 'run', 'run_id', 'notes', 'duration', 'is_active')

