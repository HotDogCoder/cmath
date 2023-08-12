from rest_framework import serializers

from apps.monitoreo.models import Answer


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['message', 'reply', 'created_at']

