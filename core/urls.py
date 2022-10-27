
from django.contrib import admin
from django.urls import path

from inventory.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', list_products),
    path('/crear/', create_product),
    path('/eliminar/<id>', delete_product),
    
]
