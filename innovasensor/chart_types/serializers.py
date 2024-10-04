from rest_framework import serializers
from .models import ChartType

class ChartTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChartType
        fields = ['id', 'text']