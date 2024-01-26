from django.db import models

# Create your models here.
from django.db import models

class Medicine(models.Model):
    name = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=0)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    expiration_date = models.DateField()

    def __str__(self):
        return self.name

class Equipment(models.Model):
    name = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=0)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_date = models.DateField()

    def __str__(self):
        return self.name

class StockLevelAlert(models.Model):
    inventory_item = models.ForeignKey('InventoryItem', on_delete=models.CASCADE)
    threshold_quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.inventory_item} - Threshold: {self.threshold_quantity}"

class PurchaseOrder(models.Model):
    inventory_item = models.ForeignKey('InventoryItem', on_delete=models.CASCADE)
    quantity_to_order = models.PositiveIntegerField()
    order_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.inventory_item} - Quantity: {self.quantity_to_order}"

class InventoryItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
