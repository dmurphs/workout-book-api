from rest_framework import serializers
from .models import Workout, Lift, LiftEntry, Set

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
        fields = ('workout','lift')

class SetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Set
        fields = ('lift_entry', 'set_num', 'num_reps', 'weight')