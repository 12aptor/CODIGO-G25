from django.urls import path
from .views import *


urlpatterns = [
    path('list/', ServiceListView.as_view()),
    path('create/', ServiceCreateView.as_view()),
    path('update/<int:pk>/', ServiceUpdateView.as_view()),

    path('barber/list/', BarberListView.as_view()),
    path('barber/create/', BarberCreateView.as_view()),
    path('barber/update/<int:pk>/', BarberUpdateView.as_view()),
    path('barber/delete/<int:pk>/', BarberDestroyView.as_view()),
    path('barber/available/<int:day>/<str:hour>/', BarberAvailableView.as_view()),

    path('schedule/list/', ScheduleListView.as_view()),
    path('schedule/create/', ScheduleCreateView.as_view()),
    path('schedule/update/<int:pk>/', ScheduleUpdateView.as_view()),
    path('schedule/delete/<int:pk>/', ScheduleDestroyView.as_view()),
]