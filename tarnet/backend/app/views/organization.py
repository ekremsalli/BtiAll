from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

from app.serializers.organization import OrganizationSerializer
from common.views import BaseView
from app.models.organization import Organization, OrganizationUser
from common.permission import IsAdmin
from app.armon_integration import ArmonApi


class OrganizationView(BaseView, APIView):
    # permission_classes = [IsAdmin]

    @swagger_auto_schema(operation_description="Organization list", tags=['Organization'])
    def get(self, request):
        d = OrganizationUser.objects.filter(user_id=request.user.id).values('organization_id_id')
        data = Organization.objects.filter(id__in=d)
        serializer = OrganizationSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class OrganizationSyncView(BaseView, APIView):
    permission_classes = [IsAdmin]

    @swagger_auto_schema(operation_description="Organization Sync", tags=['Organization'])
    def get(self, request):
        org_grant_type = ArmonApi.get_grand_type_id(username=ArmonApi.USERNAME)

        # for i in range(len(org_grant_type)):
        #     obj, created = Organization.objects.update_or_create(organization_id=org_grant_type[i].get("id"),
        #                                                          organization_name=org_grant_type[i].get("name"),
        #                                                          grant_type_id=org_grant_type[i].get("authentications")[
        #                                                              0].get("id"))

        for i in range(len(org_grant_type)):
            org_id = org_grant_type[i].get("id")
            org_name = org_grant_type[i].get("name")
            grant_type_id = org_grant_type[i].get("authentications")[0].get("id")
            
            try:
                # Eğer kayıt zaten varsa güncelle
                obj = Organization.objects.get(organization_id=org_id)
                obj.organization_name = org_name
                obj.grant_type_id = grant_type_id
                obj.save()
            except Organization.DoesNotExist:
                # Kayıt yoksa yeni kayıt olarak ekle
                Organization.objects.create(organization_id=org_id, organization_name=org_name, grant_type_id=grant_type_id)


        data = Organization.objects.all()
        serializer = OrganizationSerializer(data, many=True)
        response = {
            "status": "success",
            "data": serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)


class OrganizationListView(BaseView, APIView):
    permission_classes = (IsAdmin,)

    @swagger_auto_schema(operation_description="Organization all List", tags=['Organization'])
    def get(self, request):
        data = Organization.objects.all()
        serializer = OrganizationSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
