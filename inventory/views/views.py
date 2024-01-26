from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from inventory.models.models import Medicine, Equipment, StockLevelAlert, PurchaseOrder, InventoryItem
from inventory.serializers import (
    MedicineSerializer,
    EquipmentSerializer,
    StockLevelAlertSerializer,
    PurchaseOrderSerializer,
    InventoryItemSerializer,
)

class MedicineViewSet(viewsets.ModelViewSet):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer

class EquipmentViewSet(viewsets.ModelViewSet):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer

class StockLevelAlertViewSet(viewsets.ModelViewSet):
    queryset = StockLevelAlert.objects.all()
    serializer_class = StockLevelAlertSerializer

class PurchaseOrderViewSet(viewsets.ModelViewSet):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class InventoryItemViewSet(viewsets.ModelViewSet):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer
