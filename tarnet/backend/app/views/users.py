from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from drf_yasg.utils import swagger_auto_schema
from django.shortcuts import get_object_or_404
from django.http import Http404
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from rest_framework import generics
from django.contrib.auth import update_session_auth_hash

from app.serializers.users import CreateUserSerializer, UserListSerializer, UserDetailSerializer, \
    ChangePasswordSerializer, LoginUserSerializer, UserRoleSerializer, UserDeleteRole, UserChangePasswordSerializer
from app.serializers.organization import OrganizationSerializer
from common.views import BaseView
from app.logo_integration import LogoApi
from common.permission import IsAdmin
from app.models.organization import OrganizationUser, Organization


class UsersView(BaseView, APIView):
    permission_classes = [IsAdmin]

    @swagger_auto_schema(operation_description="User list", tags=['User'])
    def get(self, request):
        data = User.objects.all()
        serializer = UserListSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(operation_description="Create User",
                         request_body=CreateUserSerializer, tags=['User'])
    def post(self, request):
        data = request.data
        serializer = CreateUserSerializer(data=data, many=False)
        if serializer.is_valid():
            serializer.create(data)
            return Response({"message": "Successful"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetailView(BaseView, APIView):
    permission_classes = [IsAdmin]

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    @swagger_auto_schema(operation_description="User Detail", tags=['User'])
    def get(self, request, pk):
        queryset = self.get_object(pk)
        serializer = UserDetailSerializer(queryset, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(operation_description="User update", request_body=UserDetailSerializer, tags=['User'])
    def put(self, request, pk):
        queryset = self.get_object(pk)
        serializer = UserDetailSerializer(queryset, data=request.data, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(operation_description="User delete", tags=['User'])
    def delete(self, request, pk):
        queryset = self.get_object(pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ChangePasswordView(BaseView, APIView):

    @swagger_auto_schema(operation_description="Change Password", request_body=ChangePasswordSerializer, tags=['User'])
    def patch(self, request, pk):
        obj = User.objects.filter(id=pk)
        if obj.exists():
            user = User.objects.get(id=pk)
            serializer = ChangePasswordSerializer(user, data=request.data, many=False)
            if serializer.is_valid():
                serializer.save()
                response = {
                    'status': 'success',
                    'code': status.HTTP_200_OK,
                    'message': 'Password updated successfully',
                }
                return Response(response, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserChangePasswordView(BaseView, APIView):
    @swagger_auto_schema(operation_description="Kulanıcıların kendi şifresini değiştirme",
                         request_body=UserChangePasswordSerializer, tags=['User'])
    def put(self, request):
        user = request.user
        old_password = request.data.get('old_password')
        new_password = request.data.get('new_password')

        if not user.check_password(old_password):
            return Response({"error": "Eski şifreniz yanlış"}, status=400)

        user.set_password(new_password)
        user.save()
        update_session_auth_hash(request, user)
        return Response({"success": "Şifreniz başarıyla değiştirildi."}, status=200)


class LoginUserApi(APIView):
    permission_classes = (AllowAny,)

    @swagger_auto_schema(operation_description="Login", request_body=LoginUserSerializer, tags=['User'])
    def post(self, request):
        serializer = LoginUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        exists = User.objects.filter(username=data['username']).exists()

        if not exists:
            return Response({"response": "No User exist"}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.get(username=data['username'])
        if not user.check_password(data['password']):
            return Response({"response": "incorrect Password"}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=data['username'], password=data['password'])
        refresh = RefreshToken.for_user(user)
        response = {
            'access': str(refresh.access_token),
            'refresh': str(refresh),
            'user': {
                'user_id': user.id,
                'is_superuser': user.is_superuser
            }
        }
        return Response(response, status=status.HTTP_200_OK)


class UserRoleView(BaseView, APIView):

    @swagger_auto_schema(operation_description="Kullanıcalara Organizasyon ekle",
                         request_body=UserRoleSerializer, tags=['User'])
    def post(self, request):
        data = request.data
        serializer = UserRoleSerializer(data=data, many=False)
        org_ids = data.get("organization_id")
        user_id = data.get("user_id")
        user = User.objects.get(id=user_id)

        if serializer.is_valid():
            for i in org_ids:
                organization = Organization.objects.get(id=i)
                validate_data = {"organization_id": organization,
                                 "user_id": user}
                OrganizationUser.objects.create(**validate_data)
            return Response({"message": "Successful"}, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class UserRolesView(BaseView, APIView):

    @swagger_auto_schema(operation_description="User Roles", tags=['User'])
    def get(self, request, pk):
        d = OrganizationUser.objects.filter(user_id=pk).values('organization_id_id')
        data = Organization.objects.filter(id__in=d)
        serializer = OrganizationSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserRoleDelete(BaseView, APIView):
    @swagger_auto_schema(operation_description="User delete role", tags=['User'])
    def delete(self, request, user_id, organization_id):
        query = OrganizationUser.objects.filter(user_id=user_id, organization_id=organization_id)
        if query.exists():
            query.delete()
            return Response({"message": "Success"}, status=status.HTTP_200_OK)
        return Response({"message": "Not found organization or user"}, status=status.HTTP_400_BAD_REQUEST)
