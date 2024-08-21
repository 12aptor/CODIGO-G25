from django.urls import path
from .views import *


urlpatterns = [
    path('appointment/create/', AppointmentCreateView.as_view()),
    path('appointment/list/', AppointmentListView.as_view()),

    path('payment/list/', PaymentListView.as_view()),
    path('payment/create/', PaymentCreateView.as_view()),
    path('payment/update/<int:pk>/', PaymentUpdateView.as_view()),
    path('payment/delete/<int:pk>/', PaymentDestroyView.as_view()),

    path('invoice/create/', InvoiceCreateView.as_view()),
]