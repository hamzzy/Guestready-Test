from rest_framework import generics

from .models import Rental
from .serializers import RentalSerializer
# Create your views here.


class RentalList(generics.ListCreateAPIView):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer

