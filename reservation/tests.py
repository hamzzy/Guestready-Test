from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from reservation.serializers import RentalSerializer
from rest_framework.test import APITestCase

from reservation.models import Rental, Reservation
# Create your tests here.


get_rental_url = reverse('rental_list_create')
get_reservation_url = reverse('reservation_list_create')

class RentalModelTest(TestCase):
    def test_tag_model_str(self):
        task = Rental.objects.create(
            name ="rental-test1"
            
        )
        self.assertEqual(task.name, task.name)


# class RentalSerializer(TestCase):
    
#     def test_valid_rental_serializer(self):
#         valid_serializer_data = {
#             "name": "rental-100",
#         }
#         serializer = RentalSerializer(data=valid_serializer_data)
#         assert serializer.is_valid()
#         assert serializer.validated_data == valid_serializer_data
#         assert serializer.data == valid_serializer_data
#         assert serializer.errors == {}

#     def test_invalid_rental_serializer(self):
#         invalid_serializer_data = {}
#         serializer = RentalSerializer(data=invalid_serializer_data)
#         assert not serializer.is_valid()
#         assert serializer.validated_data == {}
#         assert serializer.data == invalid_serializer_data
#         assert serializer.errors == {"name": ["This field is required."]}


class RentalApiTest(APITestCase):


    def test_get_rental_list(self):
        res = self.client.get(get_rental_url)
          
        self.assertEqual(res.status_code, status.HTTP_200_OK)
  
    def test_create_rental(self):
        payload = {
            "name":"rental-4"
        }
  
        res = self.client.post(get_rental_url, payload)
  
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(res.data['name'], payload['name'])

    
    def test_validate_create(self):
        payload={}

        res = self.client.post(get_rental_url, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(res.json()['name'][0],"This field is required.")




# class ReservationModelTest(TestCase):
#     def test_tag_model_str(self):
#         task = Reservation.objects.create(
#             check_in ="",
#             check_out ="",
#             rental ="",
#         )
#         self.assertEqual(str(task), task.name)


class ReservationApiTest(APITestCase):


    def setUp(self) -> None:
        Rental.objects.create(
            name="rental-1"
        )


    def test_get_reservation_list(self):
        res = self.client.get(get_reservation_url)
          
        self.assertEqual(res.status_code, status.HTTP_200_OK)
  
    def test_create_reseervation(self):
        payload = {
            "check_in":"2022-01-03",
            "check_out":"2022-02-11",
            "rental":1
        }
  
        res = self.client.post(get_reservation_url, payload)
        print(res.data)
  
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        # self.assertEqual(res.data['name'], payload['name'])

    
    # def test_validate_create(self):
    #     payload={}

    #     res = self.client.post(get_rental_url, payload)
    #     self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
    #     self.assertEqual(res.json()['name'][0],"This field is required.")
