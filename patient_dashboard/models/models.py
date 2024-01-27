from django.db import models
import uuid
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    health_records = models.TextField() 
    
# Create your models here.
class CNFT(models.Model):
    token = models.UUIDField(default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to='cnfts/')
    uploaded_at = models.DateTimeField(auto_now_add=True)


class Image(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    metadata = models.JSONField(blank=True, null=True)     