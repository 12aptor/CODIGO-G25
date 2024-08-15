from rest_framework import serializers
from .models import *
from django.contrib.auth.hashers import make_password


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoleModel
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = MyUserModel
        fields = '__all__'

    # def create(self, validated_data):
    #     validated_data['password'] = make_password(validated_data['password'])
    #     user = MyUserModel.objects.create(**validated_data)
    #     return user
    
    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name')
    #     instance.email = validated_data.get('email')
    #     instance.phone = validated_data.get('phone')
    #     instance.status = validated_data.get('status')
    #     instance.rol_id = validated_data.get('rol_id')

    #     if 'password' in validated_data:
    #         instance.password = make_password(validated_data.get('password'))

    #     instance.save()
    #     return instance

    def save(self):
        name = self.validated_data.get('name')
        email = self.validated_data.get('email')
        phone = self.validated_data.get('phone')
        status = self.validated_data.get('status')
        rol_id = self.validated_data.get('rol_id')

        if 'password' in self.validated_data:
            password = self.validated_data.get('password')

        user = MyUserModel(
            name=name,
            email=email,
            phone=phone,
            status=status,
            rol_id=rol_id
        )
        user.set_password(password)
        user.save()
        return user