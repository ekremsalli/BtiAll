from rest_framework import serializers

from erp.models.friendly import Unitsetl

class UnitsetSerializer(serializers.ModelSerializer):
    CODE = serializers.CharField(source='code')    
    NAME = serializers.CharField(source='name')

    class Meta:
        model = Unitsetl
        fields = [
            "CODE", 
            "NAME"
        ]
