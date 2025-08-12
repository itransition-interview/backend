from rest_framework.permissions import BasePermission

from users.choices import UserRoleType


class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == UserRoleType.ADMIN.value