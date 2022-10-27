from django.contrib import admin

from inventory.models import Product
from .models import *

admin.site.register(Product)
