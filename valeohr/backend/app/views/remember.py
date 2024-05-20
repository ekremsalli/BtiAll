from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.validators import validate_email
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.models import User
from django.conf import settings


from common.views import Bti
from app.models.remember import Remember


class RememberView(Bti, APIView):
    swagger_schema = None
    authentication_classes = []
    permission_classes = ()

    def get_ip(cls, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def post(self, request, format=None, **kwargs):
        step = kwargs.get('step')
        data = request.data
        if step == '1':
            if data and data.get('email', None):
                email = data.get('email')
                try:
                    validate_email(email)
                except Exception as e:
                    print(e)
                else:
                    usr = User.objects.filter(
                        username=email).first()
                    if usr:
                        if Remember.prevent_objects.filter(
                            user=usr).exists() is False:
                            remember = Remember.generate(
                                usr,
                                self.get_ip(request)
                            )
                            remember.send()
            return Response({'continue': True})
        if step == '2':
            if data and data.get('email', None) and \
                data.get('token', None):
                email = data.get('email')
                user = User.objects.filter(username=email).first()
                token = data.get('token')
                if user and Remember.valid_objects.filter(user=user, token=token).exists():
                    return Response({'continue': True})
        if step == '3':
            if data and data.get('email', None) and \
                data.get('token', None) and data.get('new_password', None):
                email = data.get('email')
                user = User.objects.filter(username=email).first()
                token = data.get('token')
                new_password = data.get('new_password')
                if user and Remember.valid_objects.filter(user=user, token=token).exists():
                    try:
                        validate_password(new_password, user)
                    except Exception as e:
                        return Response({'continue': False, 'errors': e})
                    else:
                        user.set_password(new_password)
                        user.save()
                        Remember.objects.filter(user=user, token=token).update(
                            completed=datetime.now(), 
                            is_completed=True
                        )
                        return Response({'continue': True})

        return Response({'continue': False})
