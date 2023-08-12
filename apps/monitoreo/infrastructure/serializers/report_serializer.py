from rest_framework import serializers

from apps.monitoreo.models import Report


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ['name', 'code', 'description', 'created_at']

