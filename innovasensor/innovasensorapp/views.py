from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import generics
from .models import ChartFocus, ChartInterviewed, ChartRequirement, ChartType, Employee, UserDepartment, UserRole
from .serializers import ChartFocusSerializer, ChartInterviewedSerializer, ChartRequirementSerializer, ChartTypeSerializer, EmployeeSerializer, UserDepartmentSerializer, UserRoleSerializer


@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def user_role_list(request):
    if request.method == 'GET':
        roles = UserRole.objects.all()
        serializer = UserRoleSerializer(roles, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = UserRoleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def user_role_detail(request, pk):
    try:
        role = UserRole.objects.get(pk=pk)
    except UserRole.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserRoleSerializer(role)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserRoleSerializer(role, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        role.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def user_department_list(request):
    if request.method == 'GET':
        departments = UserDepartment.objects.all()
        serializer = UserDepartmentSerializer(departments, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = UserDepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def user_department_detail(request, pk):
    try:
        department = UserDepartment.objects.get(pk=pk)
    except UserDepartment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserDepartmentSerializer(department)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserDepartmentSerializer(department, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        department.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def employee_list(request):
    # Obtener todos los empleados
    if request.method == 'GET':
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

    # Crear un nuevo empleado
    elif request.method == 'POST':
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def employee_detail(request, pk):
    try:
        employee = Employee.objects.get(pk=pk)
    except Employee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # Obtener un empleado por ID
    if request.method == 'GET':
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

    # Actualizar un empleado
    elif request.method == 'PUT':
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Eliminar un empleado
    elif request.method == 'DELETE':
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def chart_type_list(request):
    if request.method == 'GET':
        chart_type = ChartType.objects.all()
        serializer = ChartTypeSerializer(chart_type, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ChartTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def chart_type_detail(request, pk):
    try:
        chart_type = ChartType.objects.get(pk=pk)
    except ChartType.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ChartTypeSerializer(chart_type)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ChartTypeSerializer(chart_type, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        chart_type.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def chart_requirement_list(request):
    if request.method == 'GET':
        chart_requirement = ChartRequirement.objects.all()
        serializer = ChartRequirementSerializer(chart_requirement, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ChartRequirementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def chart_requirement_detail(request, pk):
    try:
        chart_requirement = ChartRequirement.objects.get(pk=pk)
    except ChartRequirement.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ChartRequirementSerializer(chart_requirement)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ChartRequirementSerializer(chart_requirement, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        chart_requirement.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def chart_interviewed_list(request):
    if request.method == 'GET':
        chart_interviewed = ChartInterviewed.objects.all()
        serializer = ChartInterviewedSerializer(chart_interviewed, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ChartInterviewedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def chart_interviewed_detail(request, pk):
    try:
        chart_interviewed = ChartInterviewed.objects.get(pk=pk)
    except ChartInterviewed.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ChartInterviewedSerializer(chart_interviewed)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ChartInterviewedSerializer(chart_interviewed, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        chart_interviewed.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def chart_focus_list(request):
    if request.method == 'GET':
        chart_focus = ChartFocus.objects.all()
        serializer = ChartFocusSerializer(chart_focus, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ChartFocusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def chart_focus_detail(request, pk):
    try:
        chart_focus = ChartFocus.objects.get(pk=pk)
    except ChartFocus.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ChartFocusSerializer(chart_focus)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ChartFocusSerializer(chart_focus, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        chart_focus.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)