from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from onlinemarket.products.models import Category, Product
from onlinemarket.products.serializers import CategorySerializer, ProductSerializer


class CategoryList(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True, context={'request': request})
        return Response(serializer.data)

class ProductList(APIView):
    serializer_class = ProductSerializer

    def get(self, request, category_slug):
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)
        serializer = self.serializer_class(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, category_slug):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)