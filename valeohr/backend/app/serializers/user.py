from rest_framework import serializers

from django.contrib.auth.models import Permission, User

class UserSerializer(serializers.ModelSerializer):
    user_permissions = serializers.SerializerMethodField()
    groups = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = [
            "date_joined", "email", "first_name", "groups",
            "id", "is_active", "is_staff", "is_superuser",
            "last_login", "last_name", "user_permissions",
            "username"
        ]

    def get_groups(self, obj):
        groups = []
        for group in obj.groups.all():
            groups.append(group.name)
        return groups

    def get_user_permissions(self, obj):
        perms = []
        for perm in obj.user_permissions.all():
            perms.append(
                '{}.{}'.format(
                    perm.content_type.model,
                    perm.codename
                )       
            )
        return perms