from rest_framework import generics, status
from rest_framework.response import Response
from django.http import Http404
from .models import *
from .serializers import *
from authentication.permissions import (
    IsAuthenticated,
    IsAdmin,
    IsClient
)
import os
import requests
from datetime import datetime


class AppointmentCreateView(generics.CreateAPIView):
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated, IsClient]

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)

        return Response({
            'message': 'Appointment created successfully',
            'data': response.data
        }, status=status.HTTP_201_CREATED)
    
class AppointmentListView(generics.ListAPIView):
    queryset = AppointmentModel.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated, IsAdmin]

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)

        return Response({
            'message': 'Appointments fetched successfully',
            'data': response.data
        }, status=status.HTTP_200_OK)
    
class PaymentListView(generics.ListAPIView):
    queryset = PaymentModel.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated, IsAdmin]

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)

        return Response({
            'message': 'Payments fetched successfully',
            'data': response.data
        }, status=status.HTTP_200_OK)
    
class PaymentCreateView(generics.CreateAPIView):
    serializer_class = PaymentSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)

        return Response({
            'message': 'Payment created successfully',
            'data': response.data
        }, status=status.HTTP_201_CREATED)
    
class PaymentUpdateView(generics.UpdateAPIView):
    queryset = PaymentModel.objects.all()
    serializer_class = PaymentSerializer

    def update(self, request, *args, **kwargs):
        try:
            response = super().update(request, *args, **kwargs)

            return Response({
                'message': 'Payment updated successfully',
                'data': response.data
            }, status=status.HTTP_200_OK)
        except Http404:
            return Response({
                'message': 'Payment not found',
            }, status=status.HTTP_404_NOT_FOUND)
        
class PaymentDestroyView(generics.DestroyAPIView):
    queryset = PaymentModel.objects.all()

    def destroy(self, request, *args, **kwargs):
        try:
            super().destroy(request, *args, **kwargs)

            return Response({
                'message': 'Payment deleted successfully'
            }, status=status.HTTP_200_OK)
        except Http404:
            return Response({
                'message': 'Payment not found'
            }, status=status.HTTP_404_NOT_FOUND)
        
class InvoiceCreateView(generics.GenericAPIView):
    
    def post(self, request):
        try:
            url = os.environ.get('NUBEFACT_URL')
            token = os.environ.get('NUBEFACT_TOKEN')

            print(datetime.now().strftime('%d-%m-%Y'))

            invoice_data = {
                'operacion': 'generar_comprobante',
                'tipo_de_comprobante': 2,
                'serie': 'BBB1',
                'numero': 1,
                'sunat_transaction': 1,
                'cliente_tipo_de_documento': 1,
                'cliente_numero_de_documento': '00000000',
                'cliente_denominacion': 'CLIENTE DE PRUEBA',
                'cliente_direccion': 'AV. LARCO 1234',
                'cliente_email': 'email@email.com',
                'fecha_de_emision': datetime.now().strftime('%d-%m-%Y'),
                'moneda': 1,
                'porcentaje_de_igv': 18.0,
                'total': 118,
                'enviar_automaticamente_a_la_sunat': True,
                'enviar_automaticamente_al_cliente': True,
                'items': [
                    {
                        'unidad_de_medida': 'ZZ',
                        'codigo': 'C001',
                        'descripcion': 'DESCRIPCION DE PRUEBA',
                        'cantidad': 1,
                        'valor_unitario': 100,
                        'precio_unitario': 118,
                        'subtotal': 100,
                        'tipo_de_igv': 1,
                        'igv': 18,
                        'total': 118,
                        'anticipo_regularizacion': False
                    }
                ]
            }

            nubefact_response = requests.post(url=url, headers={
                'Authorization': f'Bearer {token}'
            }, json=invoice_data)

            nubefact_response_json = nubefact_response.json()

            print(nubefact_response_json)
            print(nubefact_response.status_code)

            return Response({
                'message': 'Ok'
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'message': 'Error'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        