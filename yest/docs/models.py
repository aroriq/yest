from os import name
from django.db import models

# Create your models here.
CustomerCategory=(('Rent', '賃貸'), ('Buy','購入'), ('Sell', '売却'))

class CustomerModel(models.Model):
    lastname = models.CharField(max_length=20)
    firstname = models.CharField(max_length=20)
    remarks = models.TextField()
    postdate = models.DateField(auto_now_add=True)
    category=models.CharField(
        max_length=10,
        choices=CustomerCategory
    )
    def __str__(self):
        return self.lastname

