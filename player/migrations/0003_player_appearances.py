# Generated by Django 2.1.7 on 2019-03-21 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0002_player_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='appearances',
            field=models.IntegerField(default=89),
            preserve_default=False,
        ),
    ]
