from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.http import Http404
from datetime import time
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
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)

        return Response({
            'message': 'Barbers fetched successfully',
            'data': response.data
        }, status=status.HTTP_200_OK)
    
class BarberCreateView(generics.CreateAPIView):
    serializer_class = BarberSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        response =  super().create(request, *args, **kwargs)

        return Response({
            'message': 'Barber created successfully',
            'data': response.data
        }, status=status.HTTP_201_CREATED)
    
class BarberUpdateView(generics.UpdateAPIView):
    queryset = BarberModel.objects.all()
    serializer_class = BarberSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        try:
            response = super().update(request, *args, **kwargs)

            return Response({
                'message': 'Barber updated successfully',
                'data': response.data
            }, status=status.HTTP_200_OK)
        except Http404:
            return Response({
                'message': 'Barber not found'
            }, status=status.HTTP_404_NOT_FOUND)
        
class BarberDestroyView(generics.DestroyAPIView):
    queryset = BarberModel.objects.all()
    serializer_class = BarberSerializer
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.status = False
            instance.save()

            serializer = self.get_serializer(instance)

            return Response({
                'message': 'Barber deleted successfully',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        except Http404:
            return Response({
                'message': 'Barber not found'
            }, status=status.HTTP_404_NOT_FOUND)
        
class BarberAvailableView(generics.ListAPIView):
    serializer_class = BarberSerializer

    def get_queryset(self):
        day = self.kwargs['day'] # 1, 2, 3..
        hour = self.kwargs['hour'] # 13:00 => HH:mm
        hour_time = time.fromisoformat(hour)

        avaible_barbers = BarberModel.objects.filter(
            schedules__day_of_week=day,
            schedules__start_time__lte=hour_time,
            schedules__end_time__gte=hour_time
        ).distinct()

        return avaible_barbers
    
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)

        return Response({
            'message': 'Barbers fetched successfully',
            'data': response.data
        }, status=status.HTTP_200_OK)
        
class ScheduleListView(generics.ListAPIView):
    queryset = ScheduleModel.objects.all()
    serializer_class = ScheduleSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)

        return Response({
            'message': 'Schedules fetched successfully',
            'data': response.data
        }, status=status.HTTP_200_OK)
    
class ScheduleCreateView(generics.CreateAPIView):
    serializer_class = ScheduleSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)

        return Response({
            'message': 'Schedule created successfully',
            'data': response.data
        }, status=status.HTTP_201_CREATED)
    
class ScheduleUpdateView(generics.UpdateAPIView):
    queryset = ScheduleModel.objects.all()
    serializer_class = ScheduleSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        try:
            response = super().update(request, *args, **kwargs)

            return Response({
                'message': 'Schedule updated successfully',
                'data': response.data
            }, status=status.HTTP_200_OK)
        except Http404:
            return Response({
                'message': 'Schedule not found',
            }, status=status.HTTP_404_NOT_FOUND)
        
class ScheduleDestroyView(generics.DestroyAPIView):
    queryset = ScheduleModel.objects.all()

    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)

        return Response({
            'message': 'Schedule deleted successfully',
        }, status=status.HTTP_200_OK)