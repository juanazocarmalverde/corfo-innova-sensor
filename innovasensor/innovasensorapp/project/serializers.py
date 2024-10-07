from innovasensorapp.models import Project
from rest_framework import serializers


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'code', 'justification', 'women', 'sustainable', 'url', 'success', 'success_date', 'description', 'fail']


class GETProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'code', 'justification', 'women', 'sustainable', 'url', 'success', 'success_date', 'description', 'fail']