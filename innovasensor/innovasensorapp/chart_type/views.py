from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import generics
from innovasensorapp.models import  ChartType
from .serializers import ChartTypeSerializer


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