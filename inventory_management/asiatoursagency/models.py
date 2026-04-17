from django.db import models

# Create your models here.
class Tour(models.Model):
    # we need origin country, destinaiton,number of nights, and price.
    origin_country = models.CharField(max_length=64)
    destination_country = models.CharField(max_length=64)
    number_of_nights = models.IntegerField()
    price = models.IntegerField()

#string representation of the tour
    def __str__(self):
        return (f"ID: {self.id}, Origin: {self.origin_country}, Destination: {self.destination_country}, Nights: {self.number_of_nights}, Price: {self.price}  ")