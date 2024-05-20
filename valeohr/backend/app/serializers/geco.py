from rest_framework import serializers

from app.models import GecoGroups, GecoDefs

class GecoGroupSerializer(serializers.ModelSerializer):
    source_db = serializers.StringRelatedField()
    gtype = serializers.SerializerMethodField()
    class Meta:
        model = GecoGroups
        fields = "__all__"

    def get_gtype(self, obj):
        return obj.get_gtype_display()


class GecoDefSerializer(serializers.ModelSerializer):
    source_db = serializers.StringRelatedField()
    def_type = serializers.SerializerMethodField()
    class Meta:
        model = GecoDefs
        fields = "__all__"        

    def get_def_type(self, obj):
        return obj.get_def_type_display()