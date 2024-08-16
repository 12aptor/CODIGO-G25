from rest_framework import generics, status
from rest_framework.response import Response
from django.http import Http404
from rest_framework_simplejwt.views import TokenObtainPairView
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
        try:
            response = super().update(request, *args, **kwargs)

            return Response({
                'message': 'Role updated successfully',
                'data': response.data
            }, status=status.HTTP_200_OK)
        except Http404:
            return Response({
                'message': 'Role not found'
            }, status=status.HTTP_404_NOT_FOUND)
    
class RoleDestroyView(generics.DestroyAPIView):
    queryset = RoleModel.objects.all()

    def destroy(self, request, *args, **kwargs):
        try:
            super().destroy(request, *args, **kwargs)
            
            return Response({
                'message': 'Role deleted successfully'
            }, status=status.HTTP_200_OK)
        except Http404:
            return Response ({
                'message': 'Role not found'
            }, status=status.HTTP_404_NOT_FOUND)
    
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
    
class UserUpdateView(generics.UpdateAPIView):
    queryset = MyUserModel.objects.all()
    serializer_class = UserSerializer

    def update(self, request, *args, **kwargs):
        try:
            response = super().update(request, *args, **kwargs)

            return Response({
                'message': 'User updated successfully',
                'data': response.data
            }, status=status.HTTP_200_OK)
        except Http404:
            return Response({
                'message': 'User not found'
            }, status=status.HTTP_404_NOT_FOUND)
    
class UserDestroyView(generics.DestroyAPIView):
    queryset = MyUserModel.objects.all()
    serializer_class = UserSerializer

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.status = False
            instance.save()

            serializer = self.get_serializer(instance)

            return Response({
                'message': 'User deleted successfully',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        except Http404:
            return Response({
                'message': 'User not found'
            }, status=status.HTTP_404_NOT_FOUND)
        
class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwars):
        try:
            return super().post(request, *args, **kwars)
        except ValidationError as e:
            return Response({
                'message': 'Unauthorized'
            }, status=status.HTTP_401_UNAUTHORIZED)