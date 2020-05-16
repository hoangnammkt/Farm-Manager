# Generated by Django 3.0.5 on 2020-05-09 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0018_auto_20200421_1300'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='id_farm',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='farm_id',
            field=models.CharField(default='5SUA987Z', max_length=8, unique=True),
        ),
        migrations.DeleteModel(
            name='Farm',
        ),
        migrations.DeleteModel(
            name='Staff',
        ),
    ]