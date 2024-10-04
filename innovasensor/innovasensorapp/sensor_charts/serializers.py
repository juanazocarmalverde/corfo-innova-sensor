from innovasensorapp.models import SensorChart
from rest_framework import serializers


class SensorChartSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorChart
        fields = ['id', 'executive', 'email', 'sensor_chart_date', 'first_evidence', 'second_evidence', 'third_evidence', 'comment', 'requirement_id', 'type_id', 'focus_id', 'interviewed_id', 'user_id', 'project_id']

