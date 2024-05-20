from rest_framework import serializers

from app.models import Organization


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ('id', 'organization_name', 'organization_id', 'grant_type_id')
