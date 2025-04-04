from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from products.models import Category, Product
from products.serializers import CategorySerializer, ProductSerializer
from products.filters import ProductFilter

class CategoryList(APIView):
    def get(self, request):
        if not request.query_params:
            categories = Category.objects.all()
            category_serializer = CategorySerializer(categories, many=True)
            return Response(category_serializer.data)

        products = Product.objects.all()
        filterset = ProductFilter(request.query_params, queryset=products)
        if filterset.is_valid():
            products = filterset.qs
            product_serializer = ProductSerializer(products, many=True)
            return Response(product_serializer.data, status=status.HTTP_200_OK)

class ProductList(APIView):
    serializer_class = ProductSerializer

    def get(self, request, category_slug):
        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            products = Product.objects.filter(category=category)
        else:
            products = Product.objects.all()

        filterset = ProductFilter(request.query_params, queryset=products)
        if filterset.is_valid():
            products = filterset.qs

        serializer = self.serializer_class(products, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, category_slug):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)