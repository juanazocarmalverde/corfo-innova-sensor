from innovasensorapp.models import UserDepartment
from rest_framework import serializers


class UserDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDepartment
        fields = ['id', 'name']
