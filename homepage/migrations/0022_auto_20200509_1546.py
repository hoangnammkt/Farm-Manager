# Generated by Django 3.0.5 on 2020-05-09 08:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('homepage', '0021_auto_20200509_1454'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='staff_position',
            field=models.CharField(choices=[('a', 'Quản Lý Kho'), ('b', 'Quản Lý Bán Hàng'), ('c', 'Quản Lý Sản Xuất'), ('d', 'Quản Lý Kế Toán')], default='a', max_length=100),
        ),
        migrations.AlterField(
            model_name='staff',
            name='staff_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
