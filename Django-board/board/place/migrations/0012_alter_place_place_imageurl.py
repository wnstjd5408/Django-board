# Generated by Django 3.2.8 on 2022-01-24 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0011_rename_location_id_place_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='place_imageurl',
            field=models.URLField(blank=True, max_length=300, null=True),
        ),
    ]
