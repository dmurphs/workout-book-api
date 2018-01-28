from rest_framework import permissions


class ObjectUserMatches(permissions.BasePermission):
    message = 'You don''t have access to this record'

    def has_object_permission(self, request, view, obj):
        return request.user == obj.user


class ParentWorkoutUserMatches(permissions.BasePermission):
    message = 'You don''t have access to this record'

    def has_object_permission(self, request, view, obj):
        return request.user == obj.workout.user


class ParentEntryWorkoutUserMatches(permissions.BasePermission):
    message = 'You don''t have access to this record'

    def has_object_permission(self, request, view, obj):
        return request.user == obj.lift_entry.workout.user

