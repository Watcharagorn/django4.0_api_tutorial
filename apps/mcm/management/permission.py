from rest_framework.permissions import BasePermission


class IsAdminUserOrStaff(BasePermission):
    """
    Allows access only to admin users.
    """

    def has_permission(self, request, view):
        return bool(
            request.user and request.user.is_staff and request.user.is_super_user
        )
