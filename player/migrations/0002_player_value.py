# Generated by Django 2.1.7 on 2019-03-21 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='value',
            field=models.FloatField(blank=True, null=True),
        ),
    ]