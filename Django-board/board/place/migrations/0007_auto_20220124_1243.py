# Generated by Django 3.2.8 on 2022-01-24 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0006_auto_20220124_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='place_review_blog',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='place',
            name='place_review_visit',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
