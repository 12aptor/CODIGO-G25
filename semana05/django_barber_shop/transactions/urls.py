from django.urls import path
from .views import *


urlpatterns = [
    path('appointment/create/', AppointmentCreateView.as_view()),
]