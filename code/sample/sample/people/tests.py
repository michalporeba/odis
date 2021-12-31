from datetime import date
from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient
from datetime import date
from people.models import DrivingLicense, CarOwnership, Employment
from parameterized import parameterized

# Create your tests here.

class CarOwnershipTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        seed()
    
    def test_list(self):
        response = self.client.get(reverse('cars')) 
        self.assertEqual(response.status_code, 200, 'cars endpoint should respond')
        self.assertEqual(len(response.data), 2, 'there should be two records')

    @parameterized.expand([
        ['Random', 0],
        ['First', 1],
        ['Second', 1],
        ['Owner', 2]
    ])
    def test_query(self, query, expected_count):
        response = self.client.get(reverse('cars'), {'q': query})
        self.assertEqual(response.status_code, 200, 'HTTP OK is expected')
        self.assertEqual(len(response.data), expected_count)


def seed():
    record = CarOwnership(
        date = date(2021,12,31),
        owner = 'First Owner',
        make = 'Ford',
        model = 'T',
        address = "line1",
        city = 'Abertawe',
        postcode = 'SA2 1AE'
    )
    record.save()
    record = CarOwnership(
        date = date(2022,1,1),
        owner = 'Second Owner',
        make = 'Tesla',
        model = 'T',
        address = "line2",
        city = 'Swansea',
        postcode = 'SA2 1AE'
    )
    record.save()