from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.http import Http404
from .models import *
from .serializers import *

class ServiceListView(generics.ListAPIView):
    queryset = ServiceModel.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)

        return Response({
            'message': 'Services fetched successfully',
            'data': response.data
        }, status=status.HTTP_200_OK)

class ServiceCreateView(generics.CreateAPIView):
    serializer_class = ServiceSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)

        return Response({
            'message': 'Service created successfully',
            'data': response.data
        }, status=status.HTTP_201_CREATED)
    
class ServiceUpdateView(generics.UpdateAPIView):
    queryset = ServiceModel.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        try:
            response = super().update(request, *args, **kwargs)

            return Response({
                'message': 'Service updated successfully',
                'data': response.data
            }, status=status.HTTP_200_OK)
        except Http404:
            return Response({
                'message': 'Service not found'
            }, status=status.HTTP_404_NOT_FOUND)
        

class BarberListView(generics.ListAPIView):
    queryset = BarberModel.objects.all()
    serializer_class = BarberSerializer

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)

        return Response({
            'message': 'Barbers fetched successfully',
            'data': response.data
        }, status=status.HTTP_200_OK)
    
class BarberCreateView(generics.CreateAPIView):
    serializer_class = BarberSerializer

    def create(self, request, *args, **kwargs):
        response =  super().create(request, *args, **kwargs)

        return Response({
            'message': 'Barber created successfully',
            'data': response.data
        }, status=status.HTTP_201_CREATED)
