from rest_framework import serializers
from .models import *


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceModel
        fields = '__all__'

class BarberSerializer(serializers.ModelSerializer):
    class Meta:
        model = BarberModel
        fields = '__all__'

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduleModel
        fields = '__all__'