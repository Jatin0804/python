from django.contrib import admin
from .models import Category, Product, Order

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name', 'description', 'created_at', 'updated_at']
    search_fields = ['category_name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'description', 'category', 'price', 'image', 'created_at', 'updated_at']
    search_fields = ['product_name']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer_name', 'customer_email', 'product', 'quantity', 'created_at', 'updated_at']