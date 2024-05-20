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

class IsStaff(BasePermission):
    """
    Allows access only to staff users.
    """
    def has_permission(self, request, view):
        if request.user and request.user.id:
            u = User.objects.get(pk=request.user.id)
            return u and u.is_authenticated and u.is_active and u.is_staff
        return False        

class IsUser(BasePermission):
    """
    Allows access only active users
    """
    def has_permission(self, request, view):
        if request.user and request.user.id:
            u = User.objects.get(pk=request.user.id)
            return u and u.is_authenticated and u.is_active
        return False         
class IsAdminOrChangeEditPermission(BasePermission):
    """
        Allow access only admin or users who has permissions to view
    """
    def has_permission(self, request, view):
        u = request.user
        if u and u.is_authenticated and u.is_active:
            ux = User.objects.get(pk=request.user.id)
            c1 = ux.is_superuser
            c2 = ux.has_perm('changes.edit_changes')
            return c1 or c2
        return False
