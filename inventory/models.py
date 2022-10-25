from unittest.util import _MAX_LENGTH
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=256)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    stock = models.IntegerField()
    
    def __str__(self):
        return self.name
    
