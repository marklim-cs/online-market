from django.contrib import admin
from .models import Category, Product

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description")

class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description", "price", "created_at")

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
