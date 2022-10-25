from django.shortcuts import render

from inventory.models import Product
from .models import Product
def list_products(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})
