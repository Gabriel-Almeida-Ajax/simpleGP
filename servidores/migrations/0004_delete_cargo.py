# Generated by Django 2.1 on 2018-09-11 01:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servidores', '0003_area_cargo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cargo',
        ),
    ]