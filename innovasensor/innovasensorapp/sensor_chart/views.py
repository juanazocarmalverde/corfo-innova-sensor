from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import generics
from innovasensorapp.models import SensorChart
from .serializers import SensorChartSerializer, GETSensorChartSerializer



@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def sensor_chart_list(request):
    # Obtener todos los empleados
    if request.method == 'GET':
        sensor_chart = SensorChart.objects.all()
        serializer = GETSensorChartSerializer(sensor_chart, many=True)
        return Response(serializer.data)

    # Crear un nuevo empleado
    elif request.method == 'POST':
        serializer = SensorChartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def sensor_chart_list_by_project(request, project_id):
    # Obtener todos los empleados
    try:
        sensor_chart = SensorChart.objects.filter(project_id=project_id)
    except SensorChart.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # Obtener un empleado por ID
    if request.method == 'GET':
        serializer = GETSensorChartSerializer(sensor_chart, many=True)
        return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def sensor_chart_detail(request, pk):
    try:
        sensor_chart = SensorChart.objects.get(pk=pk)
    except SensorChart.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # Obtener un empleado por ID
    if request.method == 'GET':
        serializer = GETSensorChartSerializer(sensor_chart)
        return Response(serializer.data)

    # Actualizar un empleado
    elif request.method == 'PUT':
        serializer = SensorChartSerializer(sensor_chart, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Eliminar un empleado
    elif request.method == 'DELETE':
        sensor_chart.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)