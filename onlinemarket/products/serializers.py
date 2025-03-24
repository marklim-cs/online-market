from decimal import Decimal
from rest_framework import serializers
from .models import Category, Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name", "slug"]

class ProductSerializer(serializers.ModelSerializer):
    price_after_tax = serializers.SerializerMethodField(method_name='calculate_tax')

    class Meta:
        model = Product
        fields = ["name", "description", "price", "price_after_tax", "inventory" ]

    def calculate_tax(self, product: Product):
        return product.price*Decimal("1.1")