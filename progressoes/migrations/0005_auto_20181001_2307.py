# Generated by Django 2.1 on 2018-10-02 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('progressoes', '0004_auto_20181001_2243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='progressao',
            name='tipo_progressao_tae',
            field=models.CharField(blank=True, choices=[('1', 'Progressão por Mérito'), ('2', 'Progressão por Capacitação')], max_length=1, null=True),
        ),
    ]
