from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    is_staff = models.BooleanField(default=False)


class Product(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(blank=True)
    price = models.FloatField()

    def _str_(self):
        return self.name


class OrderProduct(models.Model):
    user = models.ForeignKey(
        User,  default=1, on_delete=models.CASCADE, related_name="list")
    ordered = models.BooleanField(default=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def serialize(self):
        return {
            "username": self.user,
            "ordered": self.ordered,
            "product": self.product,
            "quantity": self.quantity,
        }


class Order(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE, related_name='users')
    lastName = models.CharField(max_length=300, default='anonimo')
    address = models.TextField(blank=True)
    phoneNumber = models.CharField(
        max_length=300, default='(593) 099 203 - 302')
    products = models.ManyToManyField(OrderProduct)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField(default=timezone.now)
    ordered = models.BooleanField(default=False)

    # def __str__(self):
    #     return self, user.username

    # def get_order(self):
    #     total = 0
    #     for order_product in self.products.all():
    #         total += order_product
    #     return total
