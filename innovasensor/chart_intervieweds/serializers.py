from rest_framework import serializers
from .models import ChartInterviewed

class ChartInterviewedSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChartInterviewed
        fields = ['id', 'text']