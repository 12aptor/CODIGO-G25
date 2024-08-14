from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .manager import UserManager


class RoleModel(models.Model):
    id = models.AutoField(primary_key=True)

    ROLE_NAME_CHOICES = [
        ('ADMIN', 'Administrador'),
        ('CLIENT', 'Cliente')
    ]

    name = models.CharField(choices=ROLE_NAME_CHOICES, default='CLIENT')

    class Meta:
        db_table = 'roles'

class MyUserModel(AbstractBaseUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, null=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_superuser = models.BooleanField(default=False)
    role_id = models.ForeignKey(RoleModel, on_delete=models.CASCADE, related_name='users', null=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'users'