# Generated by Django 4.2.1 on 2023-05-31 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_attempt_response_alter_attempt_sending_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sending',
            name='frequency',
            field=models.CharField(choices=[('Один раз', 'Один раз'), ('1 раз в день', '1 раз в день'), ('1 раз в неделю', '1 раз в неделю'), ('1 раз в месяц', '1 раз в месяц')], max_length=14, verbose_name='Периодичность'),
        ),
        migrations.AlterField(
            model_name='sending',
            name='scheduled_time',
            field=models.TimeField(auto_now_add=True, verbose_name='Время рассылки'),
        ),
    ]