from django.shortcuts import render

from inventory.models import Product
from .models import Product
def list_products(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})
def create_product(request):
    if request.method =='POST' :
        name = request.POST['name']
        price = request.POST['price']
        stock = request.POST['stock']
        product = Product(price=price, name=name, stock=stock)
        product.save()
        return redirect('/')
    else:
        return redirect('/')

def delete_product(request):
    pass        