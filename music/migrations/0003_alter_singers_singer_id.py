# Generated by Django 4.2.14 on 2024-09-06 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_alter_singers_singer_id_alter_songs_song_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='singers',
            name='singer_Id',
            field=models.ManyToManyField(related_name='singer', to='music.songs'),
        ),
    ]
