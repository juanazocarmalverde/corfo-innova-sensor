from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import generics
from .models import ChartRequirement
from .serializers import ChartRequirementSerializer


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