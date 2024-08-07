from django.urls import path
from .views import index, productos, producto

urlpatterns = [
    path('', index, name='index'),
    path('productos', productos, name='productos'),
    path('producto/<int:id>', producto, name='producto'),
]