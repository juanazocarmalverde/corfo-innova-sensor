from innovasensorapp.models import ChartType
from rest_framework import serializers


class ChartTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChartType
        fields = ['id', 'text']

