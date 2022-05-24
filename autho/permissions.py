from rest_framework import permissions


class IsAdminMember(permissions.BasePermission):

    def has_permission(self, request, view):
        if not request.user.is_admin:
            return False
        return True
