from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price', 'category', 'available_quantity')
    search_fields = ('name', 'category')
    # Добавьте другие поля, которые вы хотите видеть в админке

admin.site.register(Product, ProductAdmin)
