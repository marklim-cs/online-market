from django.urls import path
from .views import CategoryList, ProductList

urlpatterns = [
    path('categories/', CategoryList.as_view(), name='categories'),
    path('categories/<slug:category_slug>/', ProductList.as_view(), name='product-list' )
]