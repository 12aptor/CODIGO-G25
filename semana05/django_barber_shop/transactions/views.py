from rest_framework import generics, status
from .models import *
from .serializers import *


class AppointmentCreateView(generics.CreateAPIView):
    serializer_class = AppointmentSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)

        return response({
            'message': 'Appointment created successfully',
            'data': response.data
        }, status=status.HTTP_201_CREATED)