from django.db import models
from services.models import ServiceModel, BarberModel
from authentication.models import MyUserModel


class AppointmentModel(models.Model):
    id = models.AutoField(primary_key=True)
    appointment_date = models.DateTimeField()
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_id = models.ForeignKey(MyUserModel, on_delete=models.CASCADE, related_name='appointments')
    barber_id = models.ForeignKey(BarberModel, on_delete=models.CASCADE, related_name='appointments')
    service_id = models.ForeignKey(ServiceModel, on_delete=models.CASCADE, related_name='appointments')

    class Meta:
        db_table = 'appointments'

class PaymentModel(models.Model):
    id = models.AutoField(primary_key=True)
    amount = models.FloatField()

    PAYMENT_METHOD_CHOICES = [
        ('CASH', 'Efectivo'),
        ('CARD', 'Tarjeta')
    ]

    payment_menthod = models.CharField(choices=PAYMENT_METHOD_CHOICES)
    payment_date = models.DateTimeField(auto_now_add=True)
    appointment_id = models.ForeignKey(AppointmentModel, on_delete=models.CASCADE, related_name='payments')

    class Meta:
        db_table = 'payments'