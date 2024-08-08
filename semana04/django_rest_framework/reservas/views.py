from rest_framework import generics
# from rest_framework.generics import (
#     ListAPIView, # Lista de todos los objetos
#     CreateAPIView, # Permite crear un nuevo objeto
#     UpdateAPIView, # Permite actualizar un objeto por su id
#     DestroyAPIView, # Permite eliminar un objeto por su id
#     ListCreateAPIView, # Lista de todos los objetos y permite crear nuevos objetos
#     RetrieveAPIView, # Permite obtener un objeto por su id
#     RetrieveDestroyAPIView, # Permite obtener un objeto y eliminarlo por su id
#     RetrieveUpdateDestroyAPIView, # Permite obtener un objeto, actualizarlo y eliminarlo por su id
# )
from .models import CanchaModel
from .serializer import CanchaSerializer


class CanchaListView(generics.ListCreateAPIView):
    queryset = CanchaModel.objects.all()
    serializer_class = CanchaSerializer

class CanchaCreateView(generics.CreateAPIView):
    queryset = CanchaModel.objects.all()
    serializer_class = CanchaSerializer

    def create(self, request, *args, **kwargs):
        print(request.headers)
        return super().create(request, *args, **kwargs)
