from django.shortcuts import render
from django.http import JsonResponse
from .models import ProductModel

def index(request):
    context = {
        'id': 1,
        'name': 'Producto 1',
    }
    return render(request, 'index.html', context=context)

def productos(request):
    data = {
        'id': 1,
        'name': 'Producto 1',
    }
    return JsonResponse(data)

def producto(request, id):
    producto = ProductModel.objects.get(id=id)
    print(producto)
    return render(request, 'index.html')