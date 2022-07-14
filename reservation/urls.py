from django.urls import path
from .views import RentalList, ReservationView

urlpatterns = [

path("rental", RentalList.as_view(), name="rental_list_create"),
path("reservation", ReservationView.as_view(), name="reservation_list_create"),


]
