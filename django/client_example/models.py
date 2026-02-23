from django.contrib.auth.models import AbstractUser
from django.db import models


class Client(AbstractUser):

    phone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.username


class Product(models.Model):

    name = models.CharField(max_length=255)

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    def __str__(self):
        return self.name


class Order(models.Model):

    STATUS_CHOICES = [
        ("new", "Нове"),
        ("processing", "В обробці"),
        ("sent", "Відправлено"),
        ("completed", "Завершено"),
        ("cancelled", "Скасовано"),
    ]

    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name="orders"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="new"
    )

    comment = models.TextField(blank=True)

    def __str__(self):
        return f"Order #{self.id}"


    @property
    def total_price(self):

        return sum(
            item.total_price
            for item in self.items.all()
        )


class OrderProduct(models.Model):

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="items"
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    quantity = models.PositiveIntegerField(default=1)


    @property
    def total_price(self):

        return self.product.price * self.quantity


    def __str__(self):
        return f"{self.product.name} x {self.quantity}"