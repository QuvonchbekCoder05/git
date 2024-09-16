
from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

def validate_price(value):
    if value < 1 or value > 10000:
        raise ValidationError('Price must be between 1 and 10,000.')

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255 )
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[validate_price])
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.name
