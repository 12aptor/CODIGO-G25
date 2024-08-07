from django.contrib import admin
from .models import ProductModel


class ProductModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'status', 'created_at')
    search_fields = ('name',)
    list_per_page = 20


admin.site.register(ProductModel, ProductModelAdmin)