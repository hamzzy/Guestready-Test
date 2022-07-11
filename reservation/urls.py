from django.urls import path
from .views import RentalList

urlpatterns = [

path("rental", RentalList.as_view(), name="rental_list"),

]
