from rest_framework import serializers

from src.apps.vps.models import VPS


class VPSSerializer(serializers.ModelSerializer):
    uid = serializers.IntegerField(help_text="UID", required=True)
    status = serializers.IntegerField(help_text='status', allow_null=True)

    class Meta:
        model = VPS
        fields = '__all__'
