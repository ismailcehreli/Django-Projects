# Generated by Django 4.1.2 on 2022-10-10 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0002_airport_alter_flight_destination_alter_flight_origin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airport',
            name='code',
            field=models.CharField(max_length=5),
        ),
    ]
