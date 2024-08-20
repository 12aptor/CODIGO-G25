from rest_framework import generics, status
from rest_framework.response import Response
from django.http import Http404
from .models import *
from .serializers import *
from authentication.permissions import (
    IsAuthenticated,
    IsAdmin,
    IsClient
)


class AppointmentCreateView(generics.CreateAPIView):
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated, IsClient]

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)

        return Response({
            'message': 'Appointment created successfully',
            'data': response.data
        }, status=status.HTTP_201_CREATED)
    
class AppointmentListView(generics.ListAPIView):
    queryset = AppointmentModel.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated, IsAdmin]

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)

        return Response({
            'message': 'Appointments fetched successfully',
            'data': response.data
        }, status=status.HTTP_200_OK)
    
class PaymentListView(generics.ListAPIView):
    queryset = PaymentModel.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated, IsAdmin]

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)

        return Response({
            'message': 'Payments fetched successfully',
            'data': response.data
        }, status=status.HTTP_200_OK)
    
class PaymentCreateView(generics.CreateAPIView):
    serializer_class = PaymentSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)

        return Response({
            'message': 'Payment created successfully',
            'data': response.data
        }, status=status.HTTP_201_CREATED)
    
class PaymentUpdateView(generics.UpdateAPIView):
    queryset = PaymentModel.objects.all()
    serializer_class = PaymentSerializer

    def update(self, request, *args, **kwargs):
        try:
            response = super().update(request, *args, **kwargs)

            return Response({
                'message': 'Payment updated successfully',
                'data': response.data
            }, status=status.HTTP_200_OK)
        except Http404:
            return Response({
                'message': 'Payment not found',
            }, status=status.HTTP_404_NOT_FOUND)
        
class PaymentDestroyView(generics.DestroyAPIView):
    queryset = PaymentModel.objects.all()

    def destroy(self, request, *args, **kwargs):
        try:
            super().destroy(request, *args, **kwargs)

            return Response({
                'message': 'Payment deleted successfully'
            }, status=status.HTTP_200_OK)
        except Http404:
            return Response({
                'message': 'Payment not found'
            }, status=status.HTTP_404_NOT_FOUND)