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
from .models import *
from .serializer import *


class CanchaListView(generics.ListAPIView):
    queryset = CanchaModel.objects.all()
    serializer_class = CanchaSerializer

class CanchaCreateView(generics.CreateAPIView):
    queryset = CanchaModel.objects.all()
    serializer_class = CanchaSerializer
    
class CanchaRetrieveView(generics.RetrieveAPIView):
    queryset = CanchaModel.objects.all()
    serializer_class = CanchaSerializer

class CanchaUpdateView(generics.UpdateAPIView):
    queryset = CanchaModel.objects.all()
    serializer_class = CanchaSerializer

class CanchaDestroyView(generics.DestroyAPIView):
    queryset = CanchaModel.objects.all()
    serializer_class = CanchaSerializer

class CanchaRetrieveByNameView(generics.ListAPIView):
    serializer_class = CanchaSerializer

    # Podemos personalizar el queryset para que filtre el nombre de la cancha
    def get_queryset(self):
        nombre = self.kwargs.get('nombre') # self.kwargs['nombre']
        return CanchaModel.objects.filter(nombre__icontains=nombre).order_by('-id')


# Views para reservas
class ReservaListView(generics.ListAPIView):
    queryset = ReservaModel.objects.all()
    serializer_class = ReservaSerializer

class ReservaCreateView(generics.CreateAPIView):
    queryset = ReservaModel.objects.all()
    serializer_class = ReservaSerializer

class ReservaRetrieveView(generics.RetrieveAPIView):
    queryset = ReservaModel.objects.all()
    serializer_class = ReservaSerializer

class ReservaUpdateView(generics.UpdateAPIView):
    queryset = ReservaModel.objects.all()
    serializer_class = ReservaSerializer

class ReservaDestroyView(generics.DestroyAPIView):
    queryset = ReservaModel.objects.all()
    serializer_class = ReservaSerializer