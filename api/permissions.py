from rest_framework import permissions

class UserMatches(permissions.BasePermission):
    message = 'You don''t have access to this record'

    def has_object_permission(self, request, view, obj):
        return request.user == obj.user