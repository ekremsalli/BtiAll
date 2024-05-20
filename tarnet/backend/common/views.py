from rest_framework_simplejwt.authentication import JWTAuthentication, JWTTokenUserAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny

from .serializer import MyTokenObtainPairSerializer


class BaseView(object):
    authentication_classes = [JWTAuthentication]
    permission_classes = (IsAuthenticated,)


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer
