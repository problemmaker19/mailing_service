# Generated by Django 4.1 on 2022-08-22 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mailings', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mailing',
            name='time_end',
        ),
        migrations.RemoveField(
            model_name='mailing',
            name='time_start',
        ),
    ]