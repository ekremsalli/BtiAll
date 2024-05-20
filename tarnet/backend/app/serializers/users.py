from rest_framework import serializers
from django.contrib.auth.models import User


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'is_active', 'password')
        write_only_fields = ('password',)

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserListSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.CharField()
    is_active = serializers.BooleanField()

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'is_active')


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'is_active')


class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('password',)

    def update(self, instance, validated_data):
        # instance.password = validated_data.get('password', instance.password)
        instance.set_password(validated_data['password'])
        instance.save()
        return instance


class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True)


class UserRoleSerializer(serializers.Serializer):
    user_id = serializers.IntegerField(required=True)
    organization_id = serializers.ListField(child=serializers.IntegerField())


class UserDeleteRole(serializers.Serializer):
    user_id = serializers.IntegerField(required=True)
    organization_id = serializers.IntegerField(required=True)


class UserChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)