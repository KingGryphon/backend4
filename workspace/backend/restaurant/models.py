from django.db import models
from decimal import Decimal

# Create your models here.
class Menu(models.Model):
    id=models.IntegerField(primary_key=True)
    Title=models.CharField(max_length=255)
    Price=models.DecimalField(max_digits=10, decimal_places=2)
    Inventory=models.IntegerField()

    def __str__(self):
        return "{} : {}".format(self.Title, self.Price.quantize(Decimal('0.01')))


class Booking(models.Model):
    id=models.IntegerField(primary_key=True)
    Name=models.CharField(max_length=255)
    No_of_guests=models.IntegerField()
    BookingDate=models.DateTimeField()