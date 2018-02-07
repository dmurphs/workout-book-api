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


class LiftEntrySerializer(SerializerExtensionsMixin, ModelSerializer):
    class Meta:
        model = LiftEntry
        fields = ('id', 'lift', 'notes', 'is_active')
        expandable_fields = dict(
            sets=dict(serializer=SetSerializer, many=True),
            lift=dict(serializer=LiftSerializer)
        )


class RunSerializer(ModelSerializer):
    class Meta:
        model = Run
        fields = ('id', 'name', 'distance', 'elevation_delta')


class RunEntrySerializer(SerializerExtensionsMixin, ModelSerializer):

    class Meta:
        model = RunEntry
        fields = ('id', 'run', 'notes', 'duration', 'is_active')
        expandable_fields = dict(
            run=dict(serializer=RunSerializer)
        )


class WorkoutSerializer(SerializerExtensionsMixin, ModelSerializer):

    class Meta:
        model = Workout
        fields = ('id', 'description', 'date', 'is_active', 'lift_entries')
        expandable_fields = dict(
            lift_entries=dict(serializer=LiftEntrySerializer, many=True),
            run_entries=dict(serializer=RunEntrySerializer, many=True)
        )
