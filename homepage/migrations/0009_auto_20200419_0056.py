# Generated by Django 3.0.5 on 2020-04-18 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0008_auto_20200418_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='phone_number',
            field=models.CharField(default='', max_length=12),
        ),
    ]