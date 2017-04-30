from __future__ import unicode_literals

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.CharField(max_length=50)
    img = models.TextField()
    paypal = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
