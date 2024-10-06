from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import generics
from innovasensorapp.models import ChartFocus
from .serializers import ChartFocusSerializer


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