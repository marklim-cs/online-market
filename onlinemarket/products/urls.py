from django.urls import path
from .views import list_views, cart_views

urlpatterns = [
    path('', list_views.ProductList.as_view(), name='product_'),
    path('categories/', list_views.CategoryList.as_view(), name='categories'),
    path('categories/<slug:category_slug>/', list_views.ProductList.as_view(), name='category-product-list'),
    path('cart/', cart_views.CartView.as_view(), name='cart'),
]