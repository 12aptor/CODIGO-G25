from django.db import models

class ServiceModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=200, null=True)
    price = models.FloatField()

    DURATION_CHOICES = [
        (1, '1 Hora'),
        (2, '2 Horas'),
        (3, '3 Horas'),
    ]

    duration = models.IntegerField(choices=DURATION_CHOICES)

    class Meta:
        db_table = 'services'

class BarberModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    speciality = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'barbers'

class ScheduleModel(models.Model):
    id = models.AutoField(primary_key=True)

    DAY_OF_WEEK_CHOICES = [
        (1, 'Lunes'),
        (2, 'Martes'),
        (3, 'Miercoles'),
        (4, 'Jueves'),
        (5, 'Viernes'),
        (6, 'Sábado'),
    ]

    day_of_week = models.IntegerField(choices=DAY_OF_WEEK_CHOICES)
    start_time = models.TimeField()
    end_time = models.TimeField()
    barber_id = models.ForeignKey(BarberModel, on_delete=models.CASCADE, related_name='schedules')

    class Meta:
        db_table = 'schedules'