# Generated by Django 4.2.14 on 2024-08-30 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airline', '0003_airport_duration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='airport',
            name='duration',
        ),
        migrations.AddField(
            model_name='flight',
            name='duration',
            field=models.IntegerField(default=0),
        ),
    ]
