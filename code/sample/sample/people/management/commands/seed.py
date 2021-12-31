from django.core.management.base import BaseCommand
from people.models import CarOwnership, DrivingLicense, Employment, AddressMixin
from datetime import date, timedelta
import json 
import os 

class Command(BaseCommand):
    help = "seed data for testing and demo"

    DATA_ROOT = 'sample/people/data/'
    FIRST_DAY = date(2015,1,1)

    current_car = -1
        
    def handle(self, *args, **options):
        if (CarOwnership.objects.first() == None):
            self.stdout.write('seeding data...')
            self.seed()
            self.stdout.write('done.')
        else: 
            self.stdout.write('Cannot seed the data as it already exists!')
            self.stdout.write('If you want to start fresh, start with a flush by doing:')
            self.stdout.write('  python ./manage.py flush')


    def prepare_dictionaries(self):
        self.addresses = self.get_data('addresses')
        self.cars = self.get_data('cars')
        self.employers = self.get_data('employment', 'employers')
        self.departments = self.get_data('employment', 'departments')
        self.names = self.get_data('names')
        

    def seed(self):
        self.prepare_dictionaries()
        samples = self.get_data('sample', 'people')
        car = None

        for sample in samples:
            if sample['id'] <= '0':
                continue 

            self.stdout.write('  creating ' + sample['name'])
            for car_spec in sample['cars']:
                if car == None or not car_spec.get('same', False):
                    car = self.next_car()
                    
                record = CarOwnership (
                    date = self.ts_to_date(car_spec['ts']),
                    owner = sample['name'],
                    make = car['make'],
                    model = car['model'],
                )
                self.add_address(record, car_spec['address'])
                record.save()
            
            license_spec = sample['driving-license']
            if(len(license_spec)):
                record = DrivingLicense(
                    date = self.ts_to_date(license_spec['ts']),
                    name = sample['name']
                )
                self.add_address(record, license_spec['address'])
                record.save()

            for employment_spec in sample['employment']:
                record = Employment(
                    date = self.ts_to_date(employment_spec['ts']),
                    name = sample['name'],
                    employer = self.get_by_id(self.employers, employment_spec['employer'])['name'],
                    department = self.get_by_id(self.departments, employment_spec['department'])['name']
                )
                record.save()

    def get_data(self, file: str, property: str=None):
        if property == None:
            property = file

        file = open(self.DATA_ROOT + file + '.json', 'r')
        return json.load(file)[property]


    def next_car(self) -> dict:
        self.current_car = (self.current_car + 1) % len(self.cars)
        return self.cars[self.current_car]


    def ts_to_date(self, ts) -> date:
        return self.FIRST_DAY + timedelta(days=int(ts))

    
    def add_address(self, model: AddressMixin, id: str):
        address = self.get_by_id(self.addresses, id)
        model.address = address['address']
        model.city = address['city']
        model.postcode = address['postcode']
    

    def get_by_id(self, dictionary: dict, id: str) -> dict:
        return next((x for x in dictionary if x['id'] == int(id)), {})