# Generated by Django 3.2.8 on 2022-01-24 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0008_auto_20220124_1249'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('location_name', models.CharField(max_length=200)),
                ('count', models.PositiveIntegerField(blank=True, default=0, null=True)),
            ],
        ),
    ]