from rest_framework import generics

from .models import Rental, Reservation
from .serializers import RentalSerializer,ReservationSerializer
# Create your views here.


class RentalList(generics.ListCreateAPIView):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer



class ReservationView(generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer