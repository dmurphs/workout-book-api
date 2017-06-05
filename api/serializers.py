from rest_framework import serializers
from .models import Lift, Set

class LiftSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lift
        fields = ('id', 'name', 'description')

class SetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Set
        fields = ('lift', 'entry_date', 'set_num', 'num_reps')