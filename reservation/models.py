from pyexpat import model
from django.db import models

from reservation.utils import validate_reservation_date
from rest_framework import exceptions



class Rental(models.Model):
    name = models.CharField(max_length = 255)

    def __str___(self):
            return self.name



class Reservation(models.Model):
    check_in = models.DateField()
    check_out = models.DateField()
    rental = models.ForeignKey(Rental,on_delete=models.CASCADE, related_name='reservation')
    previous_reservation_id = models.IntegerField(null=True)

    
    def create_reservation(check_reservation,checkout,rental,checkin):
        if check_reservation is None:
            reserve = Reservation.objects.create(
                check_in=checkin, check_out=checkout, rental=rental
                )
            reserve.save()
            return reserve
        elif check_reservation is not None:
            reservation_id = validate_reservation_date(
                str(check_reservation.check_out), str(checkout))
            if reservation_id:
                reserve = Reservation.objects.create(
                    check_in=checkin, check_out=checkout, rental=rental, previous_reservation_id=check_reservation.id)
                reserve.save()
                return reserve
            else:
                raise exceptions.APIException("data already exists")