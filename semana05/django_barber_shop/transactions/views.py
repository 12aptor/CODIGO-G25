from rest_framework import generics, status
from rest_framework.views import APIView
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
from django.shortcuts import get_object_or_404
import mercadopago


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

        token = os.environ.get('MERCADOPAGO_TOKEN')
        mp = mercadopago.SDK(token)

        preference = {
            'items': [
                {
                    'id': 2,
                    'title': 'Zapatillas Nike',
                    'description': 'Zapatillas urbanas color negro',
                    'quantity': 2,
                    'currency_id': 'MXN',
                    'unit_price': 1000
                }
            ],
            'back_urls': {
                'success': 'https://test_frontend.com/success',
                'pending': 'https://test_frontend.com/pending',
                'failure': 'https://test_frontend.com/failure',
            },
            'notification_url': 'https://test_backend.com/api/v1/transactions/payment/verify/'
        }

        mp_response = mp.preference().create(preference)

        # response = super().create(request, *args, **kwargs)

        return Response({
            'message': 'Payment created successfully',
            # 'data': response.data,
            'data': mp_response
        }, status=status.HTTP_201_CREATED)
    
class PaymentVerifyView(APIView):
    def post(self, request):
        print(request.data)
        print(request.query_params)

        return Response({
            'message': 'Payment verified successfully'
        }, status=status.HTTP_200_OK)
    
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
        
class InvoiceCreateView(APIView):
    
    def post(self, request, appointment_id):
        try:
            appointment = get_object_or_404(AppointmentModel, id=appointment_id)

            # subtotal = total / 1.18
            total = appointment.service_id.price
            subtotal = total / 1.18
            igv = total - subtotal

            item = {
                'unidad_de_medida': 'ZZ',
                'codigo': 'C001',
                'descripcion': appointment.service_id.description,
                'cantidad': 1,
                'valor_unitario': subtotal,
                'precio_unitario': total,
                'subtotal': subtotal,
                'tipo_de_igv': 1,
                'igv': igv,
                'total': total,
                'anticipo_regularizacion': False
            }

            url = os.environ.get('NUBEFACT_URL')
            token = os.environ.get('NUBEFACT_TOKEN')

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
                'total_gravada': subtotal,
                'total_igv': igv,
                'total': total,
                'enviar_automaticamente_a_la_sunat': True,
                'enviar_automaticamente_al_cliente': True,
                'items': [item]
            }

            nubefact_response = requests.post(
                url=url,
                headers={
                    'Authorization': f'Bearer {token}'
                },
                json=invoice_data
            )

            nubefact_response_json = nubefact_response.json()
            nubefact_response_status = nubefact_response.status_code

            if nubefact_response_status != 200:
                raise Exception(nubefact_response_json['errors'])

            return Response({
                'message': 'Invoice created successfully',
                'data': nubefact_response_json
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'message': str(e.args[0])
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class InvoiceRetrieveView(APIView):

    def get(self, request, tipo_de_comprobante: int, serie: str, numero: int):
        try:
            url = os.environ.get('NUBEFACT_URL')
            token = os.environ.get('NUBEFACT_TOKEN')

            invoice_data = {
                'operacion': 'consultar_comprobante',
                'tipo_de_comprobante': tipo_de_comprobante,
                'serie': serie,
                'numero': numero
            }

            nubefact_response = requests.post(
                url=url,
                headers={
                    'Authorization': f'Bearer {token}'
                },
                json=invoice_data
            )

            nubefact_response_status = nubefact_response.status_code
            nubefact_response_json = nubefact_response.json()

            if nubefact_response_status != 200:
                raise Exception(nubefact_response_json['errors'])
            
            return Response({
                'message': 'Invoice fetched successfully',
                'data': nubefact_response_json
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'message': str(e.args[0])
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
