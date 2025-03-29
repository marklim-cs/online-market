from django.urls import path
from .views import list_views

urlpatterns = [
    path('categories/', list_views.CategoryList.as_view(), name='categories'),
    path('categories/<slug:category_slug>/', list_views.ProductList.as_view(), name='product-list'),
]