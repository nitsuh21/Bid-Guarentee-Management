# Generated by Django 3.0.5 on 2021-01-01 21:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='daysleft',
        ),
    ]
