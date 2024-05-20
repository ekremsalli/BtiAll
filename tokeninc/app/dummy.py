from rest_framework import authentication
from rest_framework import exceptions
from django.conf import settings

class DummyAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        token = request.META.get('HTTP_AUTHORIZATION')
        if token != f"--{settings.DUMMY_PWD}":
            raise exceptions.AuthenticationFailed({
                'status': False,
                'message': 'Şifre Hatası'
            })
