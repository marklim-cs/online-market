from decimal import Decimal
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Category, Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name", "slug"]

class ProductSerializer(serializers.ModelSerializer):
    price_after_tax = serializers.SerializerMethodField(method_name='calculate_tax')

    class Meta:
        model = Product
        fields = ["id", "name", "description", "price", "price_after_tax", "inventory", "category", "image"]
        extra_kwargs = {
            "inventory": {"min_value": 0},
            "name": {"validators": [
                UniqueValidator(
                    queryset=Product.objects.all()
                    )
                ]
            }
        }

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Ooops! Price should be at least 0.1")
        return value

    def calculate_tax(self, product: Product):
        return product.price*Decimal("1.1")