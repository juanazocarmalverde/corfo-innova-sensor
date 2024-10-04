from innovasensorapp.models import ChartFocus
from rest_framework import serializers

class ChartFocusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChartFocus
        fields = ['id', 'text']