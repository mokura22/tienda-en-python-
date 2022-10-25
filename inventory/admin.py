from django.contrib import admin

from inventory.models import Product
from .models import Product

admin.site.register(Product)
