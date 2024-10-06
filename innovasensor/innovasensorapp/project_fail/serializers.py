from innovasensorapp.models import ProjectFail
from rest_framework import serializers


class ProjectFailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectFail
        fields = ['id', 'text']

