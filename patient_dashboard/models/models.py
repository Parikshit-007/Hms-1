import base64
import hashlib
import os
import uuid
from cryptography.hazmat.backends import default_backend
from django.contrib.auth.models import User

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from django.db import models
class CNFT(models.Model):
    token = models.UUIDField(default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to='cnfts/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def to_json(self):
        image_data_base64 = ""
        if self.image:
            # Read the image file
            with open(self.image.path, "rb") as f:
                image_data = f.read()
                # Encrypt the image data
                encrypted_data = self.encrypt_image_data(image_data)
                # Convert encrypted data to base64
                image_data_base64 = base64.b64encode(encrypted_data).decode('utf-8')
        return {
            "token": str(self.token),
            "imageData": image_data_base64,
            "uploaded_at": self.uploaded_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
        }
    
    def encrypt_image_data(self, image_data):
        # Derive a 256-bit key from a password (you can replace this with a more secure method)
        password = b'secret_password'
        salt = b'salt'
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        key = kdf.derive(password)
        
        # Generate a random IV (Initialization Vector)
        iv = os.urandom(16)
        
        # Create an AES cipher object
        cipher = Cipher(algorithms.AES(key), modes.CTR(iv), backend=default_backend())
        
        # Encrypt the image data
        encryptor = cipher.encryptor()
        encrypted_data = encryptor.update(image_data) + encryptor.finalize()
        
        # Prepend the IV to the encrypted data for decryption later
        encrypted_data_with_iv = iv + encrypted_data
        
        return encrypted_data_with_iv
class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    health_records = models.TextField() 