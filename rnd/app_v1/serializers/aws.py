from rest_framework import serializers

from app_v1.models import S3Resource

class S3ResourceSerializer(serializers.ModelSerializer):

    class Meta:
        model = S3Resource
        fields = [
            "pk",
            "prefix", 
            "aws_access_key", 
            "aws_access_secret", 
            "bucket",
            "region"
        ]

        extra_kwargs = {
            'aws_access_secret': {'write_only': True}
        }        
