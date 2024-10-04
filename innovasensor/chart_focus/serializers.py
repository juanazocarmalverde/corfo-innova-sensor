from rest_framework import serializers
from .models import ChartFocus

class ChartFocusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChartFocus
        fields = ['id', 'text']