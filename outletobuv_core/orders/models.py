from django.db import models
from products.models import Product
from users.models import User


class Basket(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    total_price = models.IntegerField(default=0)
    # quantity = models.PositiveSmallIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Корзина для {self.user.username}'
    
    def sum(self):
        return self.product.price * self.quantity
    

class Order(models.Model):
    basket = models.ForeignKey('Basket', on_delete=models.CASCADE)
    address = models.TextField()
    commentary = models.TextField()

