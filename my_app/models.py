from django.db import models
from django.utils import timezone

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    otchestvo = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=12)

    def __str__(self):
        return self.surname + " " + self.name + " " + self.otchestvo

class Service(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()

    def __str__(self):
        return self.name

class Contract(models.Model):
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    service = models.ForeignKey('Service', on_delete=models.CASCADE)
    status = models.CharField(max_length=15)
    date = models.DateField()

