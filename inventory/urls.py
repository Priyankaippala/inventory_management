from django.urls import path
from . import views

urlpatterns = [
    # Products URLs
    path('', views.product_list, name='product_list'),
    path('<int:pk>/', views.product_detail, name='product_detail'),
    path('new/', views.product_create, name='product_create'),

    # Supplier URLs
    path('suppliers/', views.supplier_list, name='supplier_list'),
    path('suppliers/<int:pk>/', views.supplier_detail, name='supplier_detail'),
    path('suppliers/new/', views.supplier_create, name='supplier_create'),

    # Sale Order URLs
    path('sale_orders/', views.sale_order_list, name='sale_order_list'),
    path('sale_orders/<int:pk>/', views.sale_order_detail, name='sale_order_detail'),
    path('sale_orders/new/', views.sale_order_create, name='sale_order_create'),

    # Stock Movement URLs
    path('stock_movements/', views.stock_movement_list, name='stock_movement_list'),
    path('stock_movements/new/', views.stock_movement_create, name='stock_movement_create'),
]
