from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import generics
from innovasensorapp.models import Project
from .serializers import ProjectSerializer



@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def project_list(request):
    # Obtener todos los empleados
    if request.method == 'GET':
        project = Project.objects.all()
        serializer = ProjectSerializer(project, many=True)
        return Response(serializer.data)

    # Crear un nuevo empleado
    elif request.method == 'POST':
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def project_detail(request, pk):
    try:
        project = Project.objects.get(pk=pk)
    except Project.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # Obtener un empleado por ID
    if request.method == 'GET':
        serializer = ProjectSerializer(project)
        return Response(serializer.data)

    # Actualizar un empleado
    elif request.method == 'PUT':
        serializer = ProjectSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Eliminar un empleado
    elif request.method == 'DELETE':
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)