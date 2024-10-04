from rest_framework import serializers
from .models import ChartRequirement

class ChartRequirementSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChartRequirement
        fields = ['id', 'text']