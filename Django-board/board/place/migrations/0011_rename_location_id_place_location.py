# Generated by Django 3.2.8 on 2022-01-24 05:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0010_place_location_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='place',
            old_name='location_id',
            new_name='location',
        ),
    ]
