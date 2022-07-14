from django.db.models import fields
from rest_framework import serializers
from .models import Rental, Reservation
from .utils import validate_reservation_date
from rest_framework import exceptions


class RentalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rental
        fields = ("id", 'name')


class ReservationSerializer(serializers.ModelSerializer):
    rental = RentalSerializer()

    class Meta:
        model = Reservation
        fields = ['id', 'check_in', 'check_out',
                  'previous_reservation_id', 'rental']

    def create(self, validated_data):
        checkout = validated_data.get('check_out', None)
        rental = validated_data.get('rental', None)
        checkin = validated_data.get('check_in', None)
        rental = Rental.objects.get(name=rental['name'])
        check_reservation = Reservation.objects.filter(rental=rental.id).last()
        reservation = Reservation.create_reservation(
            check_reservation, checkout, rental, checkin)
        return reservation
