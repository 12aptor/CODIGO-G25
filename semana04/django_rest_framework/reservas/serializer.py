from rest_framework import serializers
from .models import CanchaModel


class CanchaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CanchaModel
        # fields = ('id', 'nombre', 'direccion')
        fields = '__all__' # Todos los campos
        # exclude = ('estado',) # No mostrar el campo indicado en la tupla, no se puede usar junto con fields
        read_only_fields = ('estado',) # Estos campos no se pueden modificar

