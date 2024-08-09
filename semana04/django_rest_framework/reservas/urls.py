from django.urls import path
from .views import *


urlpatterns = [
    path('canchas/listar', CanchaListView.as_view()),
    path('canchas/crear', CanchaCreateView.as_view()),
    path('canchas/obtener-por-id/<int:pk>', CanchaRetrieveView.as_view()),
    path('canchas/actualizar-por-id/<int:pk>', CanchaUpdateView.as_view()),
    path('canchas/eliminar-por-id/<int:pk>', CanchaDestroyView.as_view()),
    path('canchas/buscar-por-nombre/<str:nombre>', CanchaRetrieveByNameView.as_view()),
    path('reservas/listar', ReservaListView.as_view()),
    path('reservas/crear', ReservaCreateView.as_view()),
    path('reservas/obtener-por-id/<int:pk>', ReservaRetrieveView.as_view()),
    path('reservas/actualizar-por-id/<int:pk>', ReservaUpdateView.as_view()),
    path('reservas/eliminar-por-id/<int:pk>', ReservaDestroyView.as_view()),
]