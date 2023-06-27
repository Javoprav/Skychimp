# Generated by Django 4.2.2 on 2023-06-27 14:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_alter_sending_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='sending',
            name='end_date',
            field=models.DateField(default=datetime.date.today, verbose_name='Дата окончания'),
        ),
        migrations.AddField(
            model_name='sending',
            name='start_date',
            field=models.DateField(default=datetime.date.today, verbose_name='Дата начала'),
        ),
    ]
