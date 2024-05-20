from rest_framework.permissions import BasePermission
from django.contrib.auth.models import User


class BaseModelPerm(BasePermission):
    method_mapper = {
        'GET': 'view',
        'POST': 'add',
        'PUT': 'change',
        'PATCH': 'change',
        'DELETE': 'delete'
    }

    def get_model_permission(self, method, model):
        app_label = model._meta.app_label
        model_name = model._meta.model_name
        permission_name = self.method_mapper.get(method)
        return f'{app_label}.{permission_name}_{model_name}'

    def has_permission(self, request, view):
        if request.user and request.user.id:
            u = User.objects.get(pk=request.user.id)
            if u and u.is_authenticated and u.is_active:
                if u.is_staff or u.is_superuser:
                    return True
                else:
                    permission = self.get_model_permission(
                        request.method, 
                        view.get_queryset().model
                    )
                    return request.user.has_perm(permission)
        return False


class IsApiUser(BasePermission):
    """
    Allows access only to admin users.
    """
    def has_permission(self, request, view):
        if request.user and request.user.id:
            u = User.objects.get(pk=request.user.id)
            return (u and u.is_authenticated and \
                u.is_active and u.groups.filter(name='api-user'))
        return False


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


class IsStaffOrAdmin(BasePermission):
    """
    Allows access only to staff users.
    """
    def has_permission(self, request, view):
        if request.user and request.user.id:
            u = User.objects.get(pk=request.user.id)
            return u and u.is_authenticated and u.is_active and (u.is_staff or u.is_superuser)
        return False     