from innovasensorapp.models import Employee
from innovasensorapp.user_role.serializers import UserRoleSerializer
from innovasensorapp.user_department.serializers import UserDepartmentSerializer
from innovasensorapp.user.serializers import UserSerializer
from rest_framework import serializers


class EmployeeSerializer(serializers.ModelSerializer):

    role = UserRoleSerializer(read_only=True)  # Usar serializador anidado
    department = UserDepartmentSerializer(read_only=True)  # Usar serializador anidado
    user = UserSerializer(read_only=True)  # Usar serializador anidado
    
    class Meta:
        model = Employee
        fields = ['id', 'role', 'department', 'user']

