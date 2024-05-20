from rest_framework.permissions import BasePermission
from django.contrib.auth.models import User


class IsAdmin(BasePermission):
    """
    Allows access only to admin users.
    """

    def has_permission(self, request, view):
        if request.user and request.user.id:
            u = User.objects.get(pk=request.user.id)
            return u and u.is_authenticated and u.is_active and u.is_superuser
        return False
