from rest_framework.serializers import ModelSerializer
from rest_framework_serializer_extensions.serializers import \
    SerializerExtensionsMixin
from .models import Workout, Lift, LiftEntry, Set, Run, RunEntry

# Base Serializers


class LiftSerializer(ModelSerializer):

    class Meta:
        model = Lift
        fields = ('id', 'name', 'description', 'is_active')


class SetSerializer(ModelSerializer):

    class Meta:
        model = Set
        fields = ('id', 'num_reps', 'weight', 'is_active')


class LiftEntrySerializer(ModelSerializer):
    class Meta:
        model = LiftEntry
        fields = ('id', 'lift', 'notes', 'is_active')


class RunEntrySerializer(ModelSerializer):

    class Meta:
        model = RunEntry
        fields = ('id', 'run', 'notes', 'duration', 'is_active')


class RunSerializer(ModelSerializer):
    class Meta:
        model = Run
        fields = ('id', 'name', 'distance', 'elevation_delta')
        expandable_fields = dict(run_entries=RunEntrySerializer)


class WorkoutSerializer(SerializerExtensionsMixin, ModelSerializer):

    class Meta:
        model = Workout
        fields = ('id', 'description', 'date', 'is_active', 'lift_entries')
        expandable_fields = dict(
            lift_entries=dict(serializer=LiftEntrySerializer, many=True)
        )
