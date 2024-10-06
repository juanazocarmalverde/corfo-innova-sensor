from innovasensorapp.models import ChartInterviewed
from rest_framework import serializers

class ChartInterviewedSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChartInterviewed
        fields = ['id', 'text']

