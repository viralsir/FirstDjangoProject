# Generated by Django 4.2.14 on 2024-08-30 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airline', '0002_flight'),
    ]

    operations = [
        migrations.AddField(
            model_name='airport',
            name='duration',
            field=models.IntegerField(default=0),
        ),
    ]
