from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(blank=True)
    stock = models.PositiveIntegerField()
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)
    
    def __str__(self):
        return self.name