from django import forms
from .models import Supplier, Product, SaleOrder, StockMovement

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['name', 'email', 'phone', 'address']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'category', 'price', 'stock_quantity', 'supplier']

class SaleOrderForm(forms.ModelForm):
    class Meta:
        model = SaleOrder
        fields = ['product', 'quantity', 'total_price', 'sale_date', 'status']

class StockMovementForm(forms.ModelForm):
    class Meta:
        model = StockMovement
        fields = ['product', 'quantity', 'movement_type', 'movement_date', 'notes']
