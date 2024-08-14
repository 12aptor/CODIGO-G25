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
    queryset = RoleModel.objects.all()
    serializer_class = RoleSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)

        return Response({
            'message': 'Role created successfully',
            'data': response.data
        }, status=status.HTTP_201_CREATED)