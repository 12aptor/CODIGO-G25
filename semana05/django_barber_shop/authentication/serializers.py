from rest_framework import serializers
from .models import *
from django.contrib.auth.hashers import make_password


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoleModel
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False, allow_blank=True)

    class Meta:
        model = MyUserModel
        fields = '__all__'

    # def create(self, validated_data):
    #     validated_data['password'] = make_password(validated_data['password'])
    #     user = MyUserModel.objects.create(**validated_data)
    #     return user
    
    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.phone = validated_data.get('phone', instance.phone)
    #     instance.status = validated_data.get('status', instance.status)
    #     instance.role_id = validated_data.get('role_id', instance.role_id)

    #     if 'password' in validated_data:
    #         instance.password = make_password(validated_data.get('password'))

    #     instance.save()
    #     return instance


    # Si se usa save() ya no es necesario el metodo create() y update(). Y viceversa.
    def save(self):
        if self.instance:
            instance = self.instance
            instance.name = self.validated_data.get('name', instance.name)
            instance.email = self.validated_data.get('email', instance.email)
            instance.phone = self.validated_data.get('phone', instance.phone)
            instance.status = self.validated_data.get('status', instance.status)
            instance.role_id = self.validated_data.get('role_id', instance.role_id)

            if 'password' in self.validated_data:
                instance.password = make_password(self.validated_data.get('password'))

            instance.save()

            return instance
        else:
            user = MyUserModel(**self.validated_data)
            user.set_password(self.validated_data.get('password'))
            user.save()
            return user