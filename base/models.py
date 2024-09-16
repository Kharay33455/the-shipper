from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Countries(models.Model):
    name = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name

"""Class to track model"""
class Order(models.Model):
    tracking_id = models.CharField(max_length=10)
    screen_width = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    zoom = models.FloatField(default=0.0)
    current_position = models.CharField(max_length=40)
    expected_date = models.CharField(max_length=10)


    def __str__(self):
        return self.tracking_id
    
class Quote(models.Model):
    ship_from = models.CharField(max_length=50)
    ship_to = models.CharField(max_length=50)
    weight = models.IntegerField()
    length = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return f'Quotes from {self.ship_from} to {self.ship_to} for {self.email}'
    
class Company_name(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return {self.name}

class Shipper(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'