# Generated by Django 3.0.5 on 2020-04-21 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0017_auto_20200421_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farm',
            name='id_farm',
            field=models.CharField(default='H9R0ITO3', max_length=8, unique=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='staff_id',
            field=models.CharField(default='3GB5YR6G', max_length=8, unique=True),
        ),
    ]
