from .models import ChartFocus
from .models import ChartInterviewed
from .models import ChartRequirement
from .models import ChartType
from .models import Employee
from .models import UserDepartment
from .models import UserRole
from rest_framework import serializers


class UserRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRole
        fields = ['id', 'name']

class UserDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDepartment
        fields = ['id', 'name']

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'role_id', 'department_id', 'user']

class ChartTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChartType
        fields = ['id', 'text']

class ChartRequirementSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChartRequirement
        fields = ['id', 'text']

class ChartInterviewedSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChartInterviewed
        fields = ['id', 'text']

class ChartFocusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChartFocus
        fields = ['id', 'text']