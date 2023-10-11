from django.db import models
from .product import Products
from .customer import Customer
import uuid


class Paymentmod(models.Model):
    card_holder_name = models.CharField(max_length=100, help_text="Card Holder Name")
    transaction_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    card_number = models.CharField(max_length=16, help_text="Enter Card Number")
    expiration_date = models.DateField(help_text="Expiration Date")
    cvv = models.CharField(max_length=3, help_text="CVV/CVC")
    
    def __str__(self):
         return f"{self.card_holder_name} {self.transaction_id}"
  #to save the data
    def save_data(self):
        self.save()


class Paymentmod_upi(models.Model):
    upi_id = models.CharField(max_length=30, help_text="Enter UPI ID")
    password = models.CharField(max_length=50, blank=True, null=True, help_text="Password/Pin (for Internet Banking or Wallet)")

    def __str__(self):
        return str(self.upi_id)
  #to save the data
    def save_data(self):
        self.save()