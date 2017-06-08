from rest_framework import serializers
from .models import Workout, Lift, LiftEntry, Set, RunEntry

class WorkoutSerializer(serializers.ModelSerializer):

    class Meta:
        model = Workout
        fields = ('name', 'description', 'date')

class LiftSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lift
        fields = ('id', 'name', 'description')

class LiftEntrySerializer(serializers.ModelSerializer):

    class Meta:
        model = LiftEntry
        fields = ('lift',)

class SetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Set
        fields = ('set_num', 'num_reps', 'weight')

class RunEntrySerializer(serializers.ModelSerializer):

    class Meta:
        model = RunEntry
        fields = ('notes', 'distance', 'duration', 'elevation_delta')