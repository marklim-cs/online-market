from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from products.models import Category, Product
from products.serializers import CategorySerializer, ProductSerializer
from products.services import filter_products_by_query_params

class CategoryList(APIView):
    def get(self, request):
        categories = Category.objects.all()
        category_serializer = CategorySerializer(categories, many=True)

        products = filter_products_by_query_params(request)
        if products:
            product_serializer = ProductSerializer(products, many=True)
            return Response(product_serializer.data)

        return Response(category_serializer.data)

class ProductList(APIView):
    serializer_class = ProductSerializer

    def get(self, request, category_slug):
        category = get_object_or_404(Category, slug=category_slug)
        category_name = category.name
        products = Product.objects.filter(category=category)

        filtered_products = filter_products_by_query_params(request, category=category_name)
        if filtered_products:
            products = filtered_products

        serializer = self.serializer_class(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, category_slug):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)