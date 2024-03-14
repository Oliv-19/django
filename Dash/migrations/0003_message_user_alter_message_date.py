# Generated by Django 4.2.7 on 2023-12-06 13:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dash', '0002_message_room'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='user',
            field=models.CharField(default=str, max_length=10),
        ),
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 12, 6, 9, 55, 59, 632043)),
        ),
    ]