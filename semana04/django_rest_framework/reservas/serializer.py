from rest_framework import serializers
from .models import *


class CanchaSerializer(serializers.ModelSerializer):
    # reservas = ReservaSerializer(
    #     many=True,
    #     read_only=True,
    #     # source='reservas' # Este campo es necesario solo cuando el nombre de la propiedad es diferente al related_name
    # )

    class Meta:
        model = CanchaModel
        # fields = ('id', 'nombre', 'direccion')
        fields = '__all__' # Todos los campos
        # exclude = ('estado',) # No mostrar el campo indicado en la tupla, no se puede usar junto con fields
        # read_only_fields = ('estado',) # Estos campos no se pueden modificar

class ReservaSerializer(serializers.ModelSerializer):
    cancha = CanchaSerializer(
        read_only=True,
        source='cancha_id' # Este campo es necesario solo cuando el nombre de la propiedad es diferente al nombre del campo relacionado
    )

    class Meta:
        model = ReservaModel
        fields = '__all__'