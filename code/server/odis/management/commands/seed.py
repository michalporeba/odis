from django.core.management.base import BaseCommand
from odis.models import Service, Organisation
from django_kinder_settings import settings

class Command(BaseCommand):
    help = "seed data"

    def add_arguments(self, parser):
        parser.add_argument(
            '--silent', 
            action='store_true',
            help='If the migrations have been prefviously run, simply acknowledge it'
            )

    def handle(self, *args, **options):
        if (Service.objects.first() == None):
            self.stdout.write(f'seeding data for {settings.ODIS_SERVICE_NAME}')
            self.seed()
            self.stdout.write('done.')
        else: 
            if options['silent']:
                self.stdout.write(f'Database for {settings.ODIS_SERVICE_NAME} has been seeded.')
            else: 
                self.stdout.write('''Cannot seed the data as it already exists!
If you want to start fresh, start with a flush by doing:
python ./manage.py flush --settings=config.settings.<service>''')
    
    def seed(self):
        default_organisation = Organisation(
            name = 'Distributed Information Organisation (DIO)',
            url = 'github.com/michalporeba/odis/'
        )
        default_organisation.save()
        self.stdout.write(f'created organisation with id {default_organisation.id}')
        
        Service(
            uuid = settings.ODIS_SERVICE_ID,
            name = settings.ODIS_SERVICE_NAME,
            provider = default_organisation
        ).save()