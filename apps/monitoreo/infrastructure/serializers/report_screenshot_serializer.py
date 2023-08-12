from rest_framework import serializers

from apps.monitoreo.infrastructure.serializers.report_serializer import ReportSerializer
from apps.monitoreo.infrastructure.serializers.report_type_serializer import ReportTypeSerializer
from apps.monitoreo.models import ReportScreenshot


class ReportScreenshotSerializer(serializers.ModelSerializer):
    report = ReportSerializer()
    report_type = ReportTypeSerializer()

    class Meta:
        model = ReportScreenshot
        fields = ['name', 'path', 'created_at', 'report', 'report_type']