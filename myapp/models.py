from django.db import models

# Create your models here.
class Contact(models.Model):  # Corrected `models.model` to `models.Model`
    email = models.CharField(max_length=122)
    password = models.CharField(max_length=8)  # Password field (consider using Django's built-in user model for better security)
    address1 = models.CharField(max_length=25)
    address2 = models.CharField(max_length=25)
    city = models.CharField(max_length=25)

   