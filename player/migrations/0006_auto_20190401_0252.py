# Generated by Django 2.1.7 on 2019-04-01 02:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0005_auto_20190401_0245'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='defender',
            new_name='defence',
        ),
    ]