from rest_framework import generics, status
from rest_framework.response import Response
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
from pprint import pprint


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
    serializer_class = ReservaSerializer

    def get_queryset(self):
        return ReservaModel.objects.order_by('-id')

    def list(self, request):
        pprint(request.headers)
        # Recuperamos el queryset
        queryset = self.get_queryset()
        # Recuperamos el serializer
        serializer = self.get_serializer(queryset, many=True)
        # Los objetos objetos serializados en una lista
        data = serializer.data

        for reserva in data:
            reserva['mensaje'] = 'Empezar hora exacta, no se dará minutos extra'

        return Response({
            'message': 'Lista de reservas',
            'data': data
        }, status=status.HTTP_200_OK)

class ReservaCreateView(generics.CreateAPIView):
    queryset = ReservaModel.objects.all()
    serializer_class = ReservaSerializer

    def create(self, request, *args, **kwargs):
        print(request.data)
        # Aquí podemos crear toda nuestra lógica del método
        response = super().create(request, *args, **kwargs)
        return Response({
            'message': 'Reserva creada exitosamente',
            'data': response.data
        }, status=status.HTTP_201_CREATED)

class ReservaRetrieveView(generics.RetrieveAPIView):
    queryset = ReservaModel.objects.all()
    serializer_class = ReservaSerializer

    def get_queryset(self):
        # page = self.request.query_params.get('page')
        return super().get_queryset()

    def retrieve(self, request, *args, **kwargs):
        page = request.query_params.get('page')
        print(page)
        items_per_page = request.query_params.get('itemsPerPage')
        print(items_per_page)
        return super().retrieve(request, *args, **kwargs)

class ReservaUpdateView(generics.UpdateAPIView):
    queryset = ReservaModel.objects.all()
    serializer_class = ReservaSerializer

class ReservaDestroyView(generics.DestroyAPIView):
    queryset = ReservaModel.objects.all()
    serializer_class = ReservaSerializer