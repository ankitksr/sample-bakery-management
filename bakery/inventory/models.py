import uuid

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class Ingredient(models.Model):
    """Model class to track Ingredients"""
    name = models.CharField(max_length=100)
    description = models.CharField(null=True, blank=True, max_length=1000)
    
    def __str__(self):
        return f"{self.name}"

    class Meta:
        app_label = 'inventory'


class BakeryItem(models.Model):
    """Model class to track BakeryItems"""
    name = models.CharField(max_length=100)
    ingredients = models.ManyToManyField('inventory.Ingredient', through='inventory.BakeryItemIngredient')
    cost_price = models.IntegerField()
    selling_price = models.IntegerField()

    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        app_label = 'inventory'


class BakeryItemIngredient(models.Model):
    """Intermediary model b/w BakeryItem and Ingredient"""
    bakery_item = models.ForeignKey('inventory.BakeryItem', on_delete=models.CASCADE)
    ingredient = models.ForeignKey('inventory.Ingredient', on_delete=models.CASCADE)
    quantity_percentage = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.bakery_item.name} - {self.ingredient.name}"
    
    class Meta:
        app_label = 'inventory'


class Order(models.Model):
    """Model class to track orders for BakeryItem"""
    date_created = models.DateTimeField(auto_now_add=True, blank=False)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bakeryitems = models.ManyToManyField('inventory.BakeryItem', through='inventory.OrderItem')

    def __str__(self):
        return f"{self.id}"
    
    class Meta:
        app_label = 'inventory'


class OrderItem(models.Model):
    """Intermediary model to track items in an order"""
    date_created = models.DateTimeField(auto_now_add=True, blank=False)
    order = models.ForeignKey('inventory.Order', on_delete=models.CASCADE)
    bakery_item = models.ForeignKey('inventory.BakeryItem', on_delete=models.CASCADE)
    count = models.PositiveSmallIntegerField()

    @property
    def total_price(self):
        return self.bakery_item.selling_price * self.count
    
    class Meta:
        app_label = 'inventory'



