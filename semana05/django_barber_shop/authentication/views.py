from rest_framework import generics, status
from rest_framework.response import Response
from .models import *
from .serializers import *


class RoleListView(generics.ListAPIView):
    queryset = RoleModel.objects.all()
    serializer_class = RoleSerializer

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)

        return Response({
            'message': 'Roles fetched successfully',
            'data': response.data
        }, status=status.HTTP_200_OK)
    
class RoleCreateView(generics.CreateAPIView):
    serializer_class = RoleSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)

        return Response({
            'message': 'Role created successfully',
            'data': response.data
        }, status=status.HTTP_201_CREATED)

class RoleUpdateView(generics.UpdateAPIView):
    queryset = RoleModel.objects.all()
    serializer_class = RoleSerializer

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)

        return Response({
            'message': 'Role updated successfully',
            'data': response.data
        }, status=status.HTTP_200_OK)
    
class RoleDestroyView(generics.DestroyAPIView):
    queryset = RoleModel.objects.all()

    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        
        return Response({
            'message': 'Role deleted successfully'
        }, status=status.HTTP_200_OK)
    
class UserListView(generics.ListAPIView):
    queryset = MyUserModel.objects.all()
    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)

        return Response({
            'message': 'Users fetched successfully',
            'data': response.data
        }, status=status.HTTP_200_OK)

class UserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)

        return Response ({
            'message': 'User created successfully',
            'data': response.data
        }, status=status.HTTP_201_CREATED)