import datetime
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError
from rest_framework.generics import (CreateAPIView,
                                     UpdateAPIView,
                                     ListAPIView,
                                     RetrieveAPIView)

from .models import Lift, LiftEntry, Set, Workout, Run, RunEntry
from .permissions import (ObjectUserMatches,
                          ParentWorkoutUserMatches,
                          ParentEntryWorkoutUserMatches)
from .serializers import (LiftSerializer,
                          LiftEntrySerializer,
                          SetSerializer,
                          WorkoutSerializer,
                          RunSerializer,
                          RunEntrySerializer)


# Workout Views
class CreateWorkoutView(CreateAPIView):
    permission_classes = (ObjectUserMatches,)

    serializer_class = WorkoutSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ListWorkoutsView(ListAPIView):
    permission_classes = (ObjectUserMatches,)

    serializer_class = WorkoutSerializer

    def get_queryset(self):
        default_date = datetime.datetime.now().date()

        query_params = self.request.query_params
        start_date = query_params['start_date'] \
            if 'start_date' in query_params \
            else default_date
        end_date = query_params['end_date'] \
            if 'end_date' in query_params \
            else default_date

        try:
            filtered_workouts = Workout.objects.filter(
                date__range=(start_date, end_date),
                user=self.request.user,
                is_active=True)
            return filtered_workouts.order_by('-date')

        except ValidationError as e:
            # Invalid values in query parameters
            return None


class DetailWorkoutView(RetrieveAPIView):
    permission_classes = (ObjectUserMatches,)

    serializer_class = WorkoutSerializer
    queryset = Workout.objects.filter(is_active=True)


class UpdateWorkoutView(UpdateAPIView):
    permission_classes = (ObjectUserMatches,)

    serializer_class = WorkoutSerializer
    queryset = Workout.objects.filter(is_active=True)


# Lift Views
class CreateLiftView(CreateAPIView):
    permission_classes = (ObjectUserMatches,)

    serializer_class = LiftSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ListLiftsView(ListAPIView):
    permission_classes = (ObjectUserMatches,)

    serializer_class = LiftSerializer

    def get_queryset(self):
        return Lift.objects.filter(
            user=self.request.user,
            is_active=True)


class DetailLiftView(RetrieveAPIView):
    permission_classes = (ObjectUserMatches,)

    serializer_class = LiftSerializer
    queryset = Lift.objects.filter(is_active=True)


class UpdateLiftView(UpdateAPIView):
    permission_classes = (ObjectUserMatches,)

    serializer_class = LiftSerializer
    queryset = Lift.objects.filter(is_active=True)

    # def perform_update(self,serializer):
    #     serializer.save()

    #     data = serializer.data

    #     # If lift is inactivated, need to cascade inactivate associated
    #     # lift entries
    #     if not data['is_active']:
    #         lift_id = data['id']
    #         lift_entries = LiftEntry.objects.filter(lift_id=lift_id)

    #         for lift_entry in lift_entries:
    #             lift_entry.is_active = False
    #             lift_entry.save()


# Lift Entry Views
class CreateLiftEntryView(CreateAPIView):
    permission_classes = (ParentWorkoutUserMatches,)
    serializer_class = LiftEntrySerializer

    def perform_create(self, serializer):
        workout_id = self.kwargs['workout_id']
        workout = Workout.objects.get(pk=workout_id)
        serializer.save(workout=workout)


class ListLiftEntriesView(ListAPIView):
    permission_classes = (ParentWorkoutUserMatches,)
    serializer_class = LiftEntrySerializer

    def get_queryset(self):
        workout_id = self.kwargs['workout_id']
        workout = get_object_or_404(Workout.objects.all(), pk=workout_id)
        lift_entries = LiftEntry.objects.filter(
            workout=workout,
            is_active=True,
            lift__is_active=True,
            workout__is_active=True)
        return lift_entries


class DetailLiftEntryView(RetrieveAPIView):
    permission_classes = (ParentWorkoutUserMatches,)

    serializer_class = LiftEntrySerializer
    queryset = LiftEntry.objects.filter(is_active=True,
                                        lift__is_active=True,
                                        workout__is_active=True)


class UpdateLiftEntryView(UpdateAPIView):
    permission_classes = (ParentWorkoutUserMatches,)

    serializer_class = LiftEntrySerializer
    queryset = LiftEntry.objects.filter(is_active=True,
                                        lift__is_active=True,
                                        workout__is_active=True)


# Set Views
class CreateSetView(CreateAPIView):
    permission_classes = (ParentEntryWorkoutUserMatches,)
    serializer_class = SetSerializer

    def perform_create(self, serializer):
        lift_entry_id = self.kwargs['lift_entry_id']
        lift_entry = LiftEntry.objects.get(pk=lift_entry_id)
        serializer.save(lift_entry=lift_entry)


class ListSetsView(ListAPIView):
    permission_classes = (ParentEntryWorkoutUserMatches,)
    serializer_class = SetSerializer

    def get_queryset(self):
        lift_entry_id = self.kwargs['lift_entry_id']
        lift_entry = LiftEntry.objects.get(pk=lift_entry_id)
        sets = Set.objects.filter(
            lift_entry=lift_entry,
            is_active=True,
            lift_entry__is_active=True)
        return sets


class DetailSetView(RetrieveAPIView):
    permission_classes = (ParentEntryWorkoutUserMatches,)

    serializer_class = SetSerializer
    queryset = Set.objects.filter(is_active=True, lift_entry__is_active=True)


class UpdateSetView(UpdateAPIView):
    permission_classes = (ParentEntryWorkoutUserMatches,)

    serializer_class = SetSerializer
    queryset = Set.objects.filter(is_active=True, lift_entry__is_active=True)


# Run Views
class ListRunsView(ListAPIView):
    permission_classes = (ObjectUserMatches,)

    serializer_class = RunSerializer

    def get_queryset(self):
        return Run.objects.filter(
            user=self.request.user,
            is_active=True)


# Run Entry Views
class CreateRunEntryView(CreateAPIView):
    permission_classes = (ParentWorkoutUserMatches,)
    serializer_class = RunEntrySerializer

    def perform_create(self, serializer):
        workout_id = self.kwargs['workout_id']
        workout = Workout.objects.get(pk=workout_id)
        serializer.save(workout=workout)


class ListRunEntriesView(ListAPIView):
    permission_classes = (ParentWorkoutUserMatches,)
    serializer_class = RunEntrySerializer

    def get_queryset(self):
        workout_id = self.kwargs['workout_id']
        workout = get_object_or_404(Workout.objects.all(), pk=workout_id)
        run_entries = RunEntry.objects.filter(
            workout=workout,
            is_active=True,
            workout__is_active=True)
        return run_entries


class DetailRunEntryView(RetrieveAPIView):
    permission_classes = (ParentWorkoutUserMatches,)

    serializer_class = RunEntrySerializer
    queryset = RunEntry.objects.filter(is_active=True, workout__is_active=True)


class UpdateRunEntryView(UpdateAPIView):
    permission_classes = (ParentWorkoutUserMatches,)

    serializer_class = RunEntrySerializer
    queryset = RunEntry.objects.filter(is_active=True, workout__is_active=True)

