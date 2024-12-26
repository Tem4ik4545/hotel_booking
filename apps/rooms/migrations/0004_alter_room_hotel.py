# Generated by Django 5.1.4 on 2024-12-11 23:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0001_initial'),
        ('rooms', '0003_room_hotel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='hotel',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='rooms', to='hotels.hotel'),
            preserve_default=False,
        ),
    ]
