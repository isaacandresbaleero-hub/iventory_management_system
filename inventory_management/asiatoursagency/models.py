from django.db import models

# Create your models here.
class tour(models.Model):
    # we need origin country, destinaiton,number of nights, and price.
    origin_country = models.CharField(max_length=64)
    destination_country = models.CharField(max_length=64)
    number_of_nights = models.IntegerField()
    price = models.IntegerField()