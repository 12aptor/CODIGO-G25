from django.urls import path
from .views import CanchaListView, CanchaCreateView


urlpatterns = [
    path('canchas/listar', CanchaListView.as_view()),
    path('canchas/crear', CanchaCreateView.as_view()),
]