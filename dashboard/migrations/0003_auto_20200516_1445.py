# Generated by Django 3.0.5 on 2020-05-16 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20200516_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='staff_position',
            field=models.CharField(default='', max_length=100),
        ),
    ]