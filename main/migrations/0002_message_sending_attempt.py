# Generated by Django 4.2.1 on 2023-05-28 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=254)),
                ('body', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Сообщение',
                'verbose_name_plural': 'Сообщения',
            },
        ),
        migrations.CreateModel(
            name='Sending',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('scheduled_time', models.TimeField()),
                ('frequency', models.CharField(choices=[('once', 'Once'), ('daily', 'Daily'), ('weekly', 'Weekly'), ('monthly', 'Monthly')], max_length=10)),
                ('status', models.CharField(choices=[('created', 'Created'), ('completed', 'Completed'), ('launched', 'Launched')], default='created', max_length=50)),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.message')),
            ],
            options={
                'verbose_name': 'Рассылка',
                'verbose_name_plural': 'Рассылки',
            },
        ),
        migrations.CreateModel(
            name='Attempt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sent_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('in progress', 'In Progress'), ('success', 'Success'), ('failure', 'Failure')], max_length=50)),
                ('response', models.TextField(blank=True, null=True)),
                ('sending', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.sending')),
            ],
            options={
                'verbose_name': 'Статистика (попытка)',
                'verbose_name_plural': 'Статистики (попытки)',
            },
        ),
    ]
