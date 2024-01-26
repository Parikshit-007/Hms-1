from django.contrib import admin

# Register your models here.

from inventory.models.models import Medicine, Equipment, StockLevelAlert, PurchaseOrder, InventoryItem

@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = ['name', 'manufacturer', 'quantity', 'unit_price', 'expiration_date']

@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'manufacturer', 'quantity', 'unit_price', 'purchase_date']

@admin.register(StockLevelAlert)
class StockLevelAlertAdmin(admin.ModelAdmin):
    list_display = ['inventory_item', 'threshold_quantity']

@admin.register(PurchaseOrder)
class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ['inventory_item', 'quantity_to_order', 'order_date']

@admin.register(InventoryItem)
class InventoryItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
