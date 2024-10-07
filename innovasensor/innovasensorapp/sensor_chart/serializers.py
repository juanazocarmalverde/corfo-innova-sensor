from innovasensorapp.models import SensorChart
from innovasensorapp.chart_requirement.serializers import ChartRequirementSerializer
from innovasensorapp.chart_type.serializers import ChartTypeSerializer
from innovasensorapp.chart_focus.serializers import ChartFocusSerializer
from innovasensorapp.chart_interviewed.serializers import ChartInterviewedSerializer
from innovasensorapp.employee.serializers import GETEmployeeSerializer
from innovasensorapp.project.serializers import GETProjectSerializer
from rest_framework import serializers


class SensorChartSerializer(serializers.ModelSerializer):  
    class Meta:
        model = SensorChart
        fields = ['id', 'executive', 'email', 'sensor_chart_date','first_evidence', 'second_evidence', 'third_evidence', 'comment', 'requirement', 'chart_type', 'focus', 'interviewed', 'employee', 'project']


class GETSensorChartSerializer(serializers.ModelSerializer):

    requirement = ChartRequirementSerializer(read_only=True)  # Usar serializador anidado
    chart_type = ChartTypeSerializer(read_only=True)  # Usar serializador anidado
    focus = ChartFocusSerializer(read_only=True)  # Usar serializador anidado
    interviewed = ChartInterviewedSerializer(read_only=True)  # Usar serializador anidado
    employee = GETEmployeeSerializer(read_only=True)  # Usar serializador anidado
    project = GETProjectSerializer(read_only=True)  # Usar serializador anidado

    class Meta:
        model = SensorChart
        fields = ['id', 'executive', 'email', 'sensor_chart_date','first_evidence', 'second_evidence', 'third_evidence', 'comment', 'requirement', 'chart_type', 'focus', 'interviewed', 'employee', 'project']

