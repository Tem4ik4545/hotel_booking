# Generated by Django 5.1.4 on 2024-12-10 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0001_initial'),
    ]

    operations = [


        migrations.AddField(
            model_name='booking',
            name='guests',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
