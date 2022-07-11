from pyexpat import model
from django.db import models



class Rental(models.Model):
    name = models.CharField(max_length = 255)

    def __str___(self):
            return self.name



class Reservation(models.Model):
    check_in = models.DateField()
    check_out = models.DateField()
    rental = models.ForeignKey(Rental,on_delete=models.CASCADE)
    previous_reservation_id = models.IntegerField()


