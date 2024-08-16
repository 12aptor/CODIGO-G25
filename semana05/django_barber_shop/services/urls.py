from django.urls import path
from .views import *


urlpatterns = [
    path('list/', ServiceListView.as_view()),
    path('create/', ServiceCreateView.as_view()),
    path('update/<int:pk>', ServiceUpdateView.as_view()),

    path('barber/list/', BarberListView.as_view()),
    path('barber/create/', BarberCreateView.as_view())
]