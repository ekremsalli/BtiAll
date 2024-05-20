from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework import status


from bti.views.base import Bti
from common.permissions import IsUser

from app_v1.serializers.user import UserSerializer

class Profile(Bti, APIView):
    swagger_schema = None
    authentication_classes = [JWTAuthentication]
    permission_classes = (IsUser,)

    def get(self, request, format=None):
        #update_last_login(None, request.user)
        return Response({
            'user': UserSerializer(request.user).data,
        })

class Dashboard(Bti, APIView):
    swagger_schema = None
    authentication_classes = [JWTAuthentication]
    permission_classes = (IsUser,)
    def get(self, request, format=None):
        return Response({})


class ChangePassword(Bti, APIView):
    swagger_schema = None
    authentication_classes = [JWTAuthentication]
    permission_classes = (IsUser,)
    def patch(self, request, format=None):
        from django.contrib.auth import authenticate
        import django.contrib.auth.password_validation as validators
        data = request.data
        if self.request.user is None:
            return Response({
                'status': False,
                'description': 'Lütfen giriş yapın!',
            })
        if 'current' in data and 'new' in data and 'repeat' in data:
            if data['current'] and data['new'] and data['repeat']:
                check = authenticate(username=request.user.username, password=data.get('current'))
                if check is None:
                    return Response({
                        'status': False,
                        'description': 'Mevcut şifre geçersiz!',
                    })
                else:
                    try:
                        validators.validate_password(password=data.get('new'), user=request.user)
                    except Exception as e:
                        return Response({
                            'status': False,
                            'description': e
                        })
                    else:
                        request.user.set_password(data.get('new'))
                        request.user.save()
                        return Response({
                            'status': True
                        })
            else:
                return Response({
                    'status': False,
                    'description': 'Lütfen tüm alanları doldurun!',
                })
        else:
            return Response({
                'status': False,
                'description': 'Lütfen tüm alanları doldurun!',
            })
