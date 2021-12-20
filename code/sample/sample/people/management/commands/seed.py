from django.core.management.base import BaseCommand
from people.models import Person 

class Command(BaseCommand):
    help = "seed data for testing and demo"

    def handle(self, *args, **options):
        self.stdout.write('seeding data...')
        self.seed()
        self.stdout.write('done.')

    def seed(self):
        person = Person(
            firstName='Molli',
            lastName='Fazan',
            serviceInstance = 1,
            address = '17 The Village, Powick',
            postcode = 'WR2 4QE'
        )
        person.save()

        person = Person(
            firstName='Devinne',
            lastName='Erni',
            serviceInstance = 2,
            address = '23 Hathaway Road, Lancaster',
            postcode = 'LA1 2JW'
        )
        person.save()

        person = Person(
            firstName='Zelma',
            lastName='Grelka',
            serviceInstance = 2,
            address = 'Flat 3, 130 Earls Court Road, London',
            postcode = 'W8 6QL'
        )
        person.save()

        person = Person(
            firstName='Grant',
            lastName='Spellard',
            serviceInstance = 3,
            address = 'Carreg Felin Yarrd, Llandegfan',
            postcode = 'LL59 5UL'
        )
        person.save()

        person = Person(
            firstName='Tonia',
            lastName='Kleinbaum',
            serviceInstance = 3,
            address = '9 Crosslow Bank, Emerson Valley',
            postcode = 'MK4 2HH'
        )
        person.save()

        person = Person(
            firstName='Anders',
            lastName='McCobb',
            serviceInstance = 3,
            address = '3 Royston Court, Potton',
            postcode = 'SG19 2NJ'
        )
        person.save()
