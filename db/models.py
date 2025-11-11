import sys

try:
    from django.db import models
except Exception:
    print('Exception: Django Not Found, please install it with "pip install django".')
    sys.exit()

# change Users to Products
class Products(models.Model):
    upc = models.CharField(max_length=5, unique=True)
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.name} ({self.upc}) - ${self.price}"
