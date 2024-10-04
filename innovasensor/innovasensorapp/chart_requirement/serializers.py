from innovasensorapp.models import ChartRequirement
from rest_framework import serializers

class ChartRequirementSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChartRequirement
        fields = ['id', 'text']
