# Generated by Django 2.1 on 2018-09-11 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servidores', '0007_auto_20180910_2258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='nome',
            field=models.CharField(choices=[('1', 'Docente'), ('2', 'TAE'), ('3', 'Professor Substituto'), ('4', 'TAE Exercício Provisório'), ('5', 'Docente Exercício Provisório')], max_length=30, unique=True),
        ),
    ]