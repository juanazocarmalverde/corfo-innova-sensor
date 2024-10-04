from innovasensorapp.models import UserRole
from rest_framework import serializers


class UserRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRole
        fields = ['id', 'name']

