# Generated by Django 2.0.6 on 2018-10-11 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MoviesApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='ageAllowed',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movies',
            name='yearReleased',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
