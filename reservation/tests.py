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

    def test_create_model_str(self):
        rental = Rental.objects.create(
            name="rental-test1"

        )
        self.assertEqual(rental.name, "rental-test1")


class RentalApiTest(APITestCase):

    def test_get_rental_list(self):
        res = self.client.get(get_rental_url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_create_rental(self):
        payload = {
            "name": "rental-4"
        }

        res = self.client.post(get_rental_url, payload, format="json")

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(res.data['name'], payload['name'])

    def test_validate_create(self):
        payload = {}

        res = self.client.post(get_rental_url, payload, format="json")
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(res.json()["name"][0], "This field is required.")


class ReservationModelTest(TestCase):
    def test_create_model_str(self):
        rental = Rental.objects.create(
            name="rental-test1"

        )
        reservation = Reservation.objects.create(
            check_in="2022-01-20",
            check_out="2022-02-3",
            rental=rental,
        )
        self.assertEqual(reservation.check_in, "2022-01-20")
        self.assertEqual(reservation.check_out, "2022-02-3")
        self.assertEqual(reservation.rental.id, 1)


class ReservationApiTest(APITestCase):

    def setUp(self) -> None:
        self.rental = Rental.objects.create(
            name="rental-1"
        )
        self.rental2 = Rental.objects.create(
            name="rental-2"
        )

    def test_get_reservation_list(self):
        res = self.client.get(get_reservation_url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_validate_create(self):
        payload = {}

        res = self.client.post(get_reservation_url, payload, format="json")
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        for n in res.json():
            self.assertEqual(res.json()[n][0], "This field is required.")

    def test_create_reservation(self):
        payload = {
            "check_in": "2022-01-03",
            "check_out": "2022-02-11",
            "rental": {
                "name": "rental-1"
            }
        }

        res = self.client.post(get_reservation_url, payload, format="json")
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        # self.assertDictEqual(res.data, payload)

    def test_create_reservation_with_same_date(self):
        payload = {
            "check_in": "2022-01-03",
            "check_out": "2022-02-11",
            "rental": {
                "name": "rental-1"
            }
        }

        res = self.client.post(get_reservation_url, payload, format='json')
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        res2 = self.client.post(get_reservation_url, payload, format="json")
        self.assertEqual(res2.status_code,
                         status.HTTP_400_BAD_REQUEST)
        self.assertEqual(res2.json()[0], "data already exists")

    def test_create_reservation_with_different_payload_but_same_checkout_date(self):
        """
        Test for
        """
        payload = {
            "check_in": "2022-01-13",
            "check_out": "2022-01-13",
            "rental":  {
                "name": "rental-1"
            }
        }
        payload2 = {
            "check_in": "2022-01-20",
            "check_out": "2022-02-10",
            "rental":  {
                "name": "rental-1"
            }
        }

        res = self.client.post(get_reservation_url, payload, format="json")
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        res2 = self.client.post(get_reservation_url, payload2, format="json")
        self.assertEqual(res2.status_code, status.HTTP_201_CREATED)

    def test_create_multiple_reservation_with_different_payload_for_previous_reservatio(self):
        """
        """
        payload = {
            "check_in": "2022-01-13",
            "check_out": "2022-01-13",
            "rental":  {
                "name": "rental-1"
            }


        }
        payload2 = {
            "check_in": "2022-01-20",
            "check_out": "2022-02-10",
            "rental":  {
                "name": "rental-1"
            }
        }
        payload3 = {
            "check_in": "2022-02-20",
            "check_out": "2022-03-10",
            "rental": {
                "name": "rental-1"
            }
        }
        res = self.client.post(get_reservation_url, payload, format="json")
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        res2 = self.client.post(get_reservation_url, payload2, format="json")
        self.assertEqual(res2.status_code, status.HTTP_201_CREATED)
        res3 = self.client.post(get_reservation_url, payload3, format="json")
        self.assertEqual(res3.status_code, status.HTTP_201_CREATED)

        payload4 = {
            "check_in": "2022-01-02",
            "check_out": "2022-01-20",
            "rental":  {
                "name": "rental-2"
            }
        }
        payload5 = {
            "check_in": "2022-01-20",
            "check_out": "2022-02-11",
            "rental":  {
                "name": "rental-2"
            }

        }
        res4 = self.client.post(get_reservation_url, payload4, format="json")
        self.assertEqual(res4.status_code, status.HTTP_201_CREATED)
        res5 = self.client.post(get_reservation_url, payload5, format="json")
        self.assertEqual(res5.status_code, status.HTTP_201_CREATED)
