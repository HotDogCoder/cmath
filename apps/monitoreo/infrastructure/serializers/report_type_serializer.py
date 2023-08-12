from rest_framework import serializers

from apps.monitoreo.models import ReportType


class ReportTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportType
        fields = ['description', 'url', 'created_at']