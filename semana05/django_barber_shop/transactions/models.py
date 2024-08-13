from django.db import models
from django.contrib.auth.models import User
from services.models import ServiceModel, BarberModel


class AppointmentModel(models.Model):
    id = models.AutoField(primary_key=True)
    appointment_date = models.DateTimeField()
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appointments')
    barber_id = models.ForeignKey(BarberModel, on_delete=models.CASCADE, related_name='appointments')
    service_id = models.ForeignKey(ServiceModel, on_delete=models.CASCADE, related_name='appointments')

    class Meta:
        db_table = 'appointments'