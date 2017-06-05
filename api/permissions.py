from rest_framework import permissions

class LiftUserMatches(permissions.BasePermission):
    message = 'You don''t have access to this record'

    def has_object_permission(self, request, view, obj):
        return request.user == obj.user

class ParentLiftUserMatches(permissions.BasePermission):
    message = 'You don''t have access to this record'

    def has_object_permission(self, request, view, obj):
        return request.user == obj.lift.user