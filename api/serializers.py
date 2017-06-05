from rest_framework import serializers
from .models import Workout, Lift

class WorkoutSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Workout
        fields = ('name', 'description')

class LiftSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lift
        fields = ('name', 'description')