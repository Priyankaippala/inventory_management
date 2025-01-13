from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Supplier, SaleOrder, StockMovement
from .forms import SupplierForm, ProductForm, SaleOrderForm, StockMovementForm



def product_list(request):
    products = Product.objects.all()
    return render(request, 'inventory/product_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'inventory/product_detail.html', {'product': product})

def product_create(request):
    if request.method == 'POST':
        # Create an instance of the form with the data from the request
        form = ProductForm(request.POST)
        
        if form.is_valid():
            # Save the new product to the database
            form.save()
            # Redirect to the product list or another success page
            return redirect('product_list')  # Redirect to the 'product_list' URL pattern
    else:
        # If the request is not POST, create an empty form
        form = ProductForm()

    return render(request, 'inventory/product_form.html', {'form': form})


# Supplier Views
def supplier_list(request):
    suppliers = Supplier.objects.all()
    return render(request, 'inventory/supplier_list.html', {'suppliers': suppliers})

def supplier_detail(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    return render(request, 'inventory/supplier_detail.html', {'supplier': supplier})

def supplier_create(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('supplier_list')
    else:
        form = SupplierForm()
    return render(request, 'inventory/supplier_form.html', {'form': form})

# Sale Order Views
def sale_order_list(request):
    sale_orders = SaleOrder.objects.all()
    return render(request, 'inventory/sale_order_list.html', {'sale_orders': sale_orders})

def sale_order_detail(request, pk):
    sale_order = get_object_or_404(SaleOrder, pk=pk)
    return render(request, 'inventory/sale_order_detail.html', {'sale_order': sale_order})

def sale_order_create(request):
    if request.method == 'POST':
        form = SaleOrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sale_order_list')
    else:
        form = SaleOrderForm()
    return render(request, 'inventory/sale_order_form.html', {'form': form})

# Stock Movement Views
def stock_movement_list(request):
    stock_movements = StockMovement.objects.all()
    return render(request, 'inventory/stock_movement_list.html', {'stock_movements': stock_movements})

def stock_movement_create(request):
    if request.method == 'POST':
        form = StockMovementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('stock_movement_list')
    else:
        form = StockMovementForm()
    return render(request, 'inventory/stock_movement_form.html', {'form': form})
