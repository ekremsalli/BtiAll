from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from django.contrib.auth.models import update_last_login

from common.views import Bti
from common.permissions import IsUser
from app.models import Excuse

from app.serializers.user import UserSerializer


class Profile(Bti, APIView):
    swagger_schema = None
    authentication_classes = [JWTAuthentication]
    permission_classes = (IsUser,)

    def get(self, request, format=None):
        update_last_login(None, request.user)
        return Response({
            'user': UserSerializer(request.user).data,
        })


class Dashboard(Bti, APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = (IsUser,)

    def get(self, request, format=None):
        from app.models import Changes

        if self.request.user.is_superuser:
            return Response({
                'changes_for_approve': Changes.waiting_for_approve.count() + Excuse.waiting_for_approve.count(),
                'changes_for_send': Changes.waiting_for_send.count() + Excuse.waiting_for_send.count()
            })
        return Response({})
