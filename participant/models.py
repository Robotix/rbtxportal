from django.db import models
from address.models import Address

# Create your models here.

class Participant(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    mobileNo = models.CharField(max_length=13)
    emailID= models.EmailField()
    college = models.CharField(max_length=100)
    address = models.ForeignKey(Address)