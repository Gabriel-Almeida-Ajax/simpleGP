# Generated by Django 2.1 on 2018-09-25 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servidores', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servidor',
            name='nome',
            field=models.CharField(help_text='Obrigatório', max_length=50),
        ),
    ]