from django.db import models
from django.conf import settings
from products.models import Product
from django.db.models import Sum

class Order(models.Model):
    id_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_order = models.DateField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=8, decimal_places=2)
    
    def update_total_amount(self):
        total = self.items.aggregate(total=Sum('total_price'))['total'] or 0
        self.total_amount = total
        self.save()

    
    def __str__(self):
        return f"Orden #{self.id} de {self.id_user.first_name}"
    

class OrderItem(models.Model):
    id_order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    unitary_price = models.FloatField()
    total_price = models.FloatField()
    
    def save(self, *args, **kwargs):
        self.unitary_price = self.id_product.price
        
        product = self.id_product
        
        if product.stock >= self.quantity:
            product.stock -= self.quantity
            product.save()
        else:
            raise ValueError("No hay suficiente stock para este producto")
    
        self.total_price = self.unitary_price * self.quantity
    
        super(OrderItem, self).save(*args, **kwargs)
        self.id_order.update_total_amount()
        
    def __str__(self):
        return f"{self.quantity} x {self.id_product.name}"