import yaml
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import exceptions
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from bti.views.base import Bti, Pagination
from portal.serializers.user import UserSerializer
from portal.permissions import IsStaff

class Profile(Bti, APIView):
    swagger_schema = None
    authentication_classes = [JWTAuthentication]
    permission_classes = (IsStaff,)
    serializer_class = UserSerializer

    def get(self, request, format=None):
        return Response({
            'user': UserSerializer(request.user).data,
        })
