# Generated by Django 4.2.4 on 2024-04-10 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AQI', '0002_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
    ]