# Generated by Django 4.0.1 on 2022-02-01 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('odis', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connection',
            name='state',
            field=models.CharField(choices=[('A', 'Active'), ('D', 'Denied'), ('F', 'Failed'), ('R', 'Requested'), ('S', 'Suspended'), ('U', 'Unavailable'), ('X', 'Disconnected')], default='R', max_length=1),
        ),
    ]