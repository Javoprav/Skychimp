# Generated by Django 4.2.2 on 2023-06-22 13:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0010_alter_customer_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='sending',
            name='created',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='clients', to=settings.AUTH_USER_MODEL, verbose_name='Кем создано'),
        ),
    ]