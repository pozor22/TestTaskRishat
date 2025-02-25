from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Order(models.Model):
    items = models.ManyToManyField(Item)

    def get_total_price(self):
        return sum(item.price for item in self.items.all())

    def __str__(self):
        return f"Order {self.id} - {self.get_total_price()} cents"
