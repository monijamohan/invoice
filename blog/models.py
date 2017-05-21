from django.db import models
from django.contrib.auth.models import User

 


class Customer(models.Model):
     full_name = models.CharField(max_length=250)
     phone_number = models.CharField(max_length=500)
     adress = models.CharField(max_length=500)
     email_ID = models.CharField(max_length=1000)
     Pincode = models.CharField(max_length=100)

     def __str__(self):
         return self.full_name

class Product(models.Model):
     item = models.CharField(max_length=250)
     quantity = models.CharField(max_length=500)
     price = models.CharField(max_length=500)
     
     def __str__(self):
         return self.item

