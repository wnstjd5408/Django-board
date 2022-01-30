# Generated by Django 3.2.8 on 2022-01-27 08:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import hitcount.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('ip', models.GenericIPAddressField()),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('comment', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='작성자')),
            ],
            bases=(models.Model, hitcount.models.HitCountMixin),
        ),
    ]
