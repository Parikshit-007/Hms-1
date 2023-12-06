from django.db import models
from cryptography.fernet import Fernet


key = b'your_generated_key_here'
cipher_suite = Fernet(key)

class Patient(models.Model):
    patient_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    health_record = models.ImageField()

    def set_health_record(self, data):
        encrypted_data = cipher_suite.encrypt(data.encode())
        self.health_record = encrypted_data

    def get_health_record(self):
        decrypted_data = cipher_suite.decrypt(self.health_record).decode()
        return decrypted_data

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
