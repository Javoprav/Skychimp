# Generated by Django 4.2.1 on 2023-05-28 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_sending_frequency_alter_sending_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attempt',
            name='status',
            field=models.CharField(choices=[('в процессе', 'В процессе'), ('успешно', 'Успешно'), ('не удачно', 'Не удачно')], max_length=50),
        ),
    ]
