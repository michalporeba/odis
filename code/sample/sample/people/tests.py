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
        seed_cars()
    
    def test_list(self):
        response = self.client.get(reverse('cars')) 
        self.assertEqual(response.status_code, 200, 'cars endpoint should respond')
        self.assertEqual(len(response.data), 2, 'there should be two records')

    @parameterized.expand([
        ['Random', 0, None],
        ['First', 1, 'First Owner'],
        ['Second', 1, 'Second Owner'],
        ['Owner', 2, 'First Owner']
    ])
    def test_query(self, query, expected_count, expected_name):
        response = self.client.get(reverse('cars'), {'q': query})
        self.assertEqual(response.status_code, 200, 'HTTP OK is expected')
        self.assertEqual(len(response.data), expected_count)
        if not expected_name is None:
            self.assertEqual(response.data[0]['owner'], expected_name)


class DrivingLicenseTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        seed_licenses()

    def test_list(self):
        response = self.client.get(reverse('licenses'))
        self.assertEqual(response.status_code, 200, 'HTTP OK is expected')
        self.assertEqual(len(response.data), 4)

    @parameterized.expand([
        ['random', 0, None],
        ['1', 1, 'Driver 1'],
        ['3', 1, 'Gyrrwr 3'],
        ['Gyrrwr', 2, 'Gyrrwr 3'],
        ['r', 4, 'Driver 1']
    ])
    def ctest_query(self, query, expected_count, expected_name):
        response = self.client.get(reverse('licenses'), {'q': query})
        print(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), expected_count)
        if not expected_name is None:
            self.assertEqual(response.data[0]['name'], expected_name)

class EmployemntTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        seed_employment()

    def test_list(self):
        response = self.client.get(reverse('employment'))
        self.assertEqual(response.status_code, 200, 'employment endpoint should response')
        self.assertEqual(len(response.data), 3, 'there should be three records exactly')

    @parameterized.expand([
        ['Random', 0, None],
        ['One', 2, 'Employee One'],
        ['Two', 1, 'Employee Two'],
        ['Employee', 3, 'Employee One']
    ])
    def test_query(self, query, expected_count, expected_name):
        response = self.client.get(reverse('employment'), {'q': query})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), expected_count)
        if not expected_name is None:
            self.assertEqual(response.data[0]['name'], expected_name)


def seed_cars():
    CarOwnership(
        date = date(2021,12,31),
        owner = 'First Owner',
        make = 'Ford',
        model = 'T',
        address = "line1",
        city = 'Abertawe',
        postcode = 'SA2 1AE'
    ).save()
    CarOwnership(
        date = date(2022,1,1),
        owner = 'Second Owner',
        make = 'Tesla',
        model = 'T',
        address = "line2",
        city = 'Swansea',
        postcode = 'SA2 1AE'
    ).save()


def seed_employment():
    Employment(
        date = date(2020,3,4),
        name = "Employee One",
        department = "Dep1",
        employer = "Google"
    ).save()
    Employment(
        date = date(2020,9,30),
        name = "Employee One",
        department = "Dep2",
        employer = "Google"
    ).save()
    Employment(
        date = date(2021,7,7),
        name = "Employee Two",
        department = "Marketing",
        employer = "Microsoft"
    ).save()


def seed_licenses():
    DrivingLicense(
        date = date(2020,3,23),
        name = "Driver 1",
    ).save()
    DrivingLicense(
        date = date(2020,9,22),
        name = "Driver 2"
    ).save()
    DrivingLicense(
        date = date(2021,1,6),
        name = "Gyrrwr 3"
    ).save()
    DrivingLicense(
        date = date(2021,12,8),
        name = "Gyrrwr 4"
    ).save()    