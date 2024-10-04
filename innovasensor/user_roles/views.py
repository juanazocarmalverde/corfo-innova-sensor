from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import generics
from .models import UserRole
from .serializers import UserRoleSerializer


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