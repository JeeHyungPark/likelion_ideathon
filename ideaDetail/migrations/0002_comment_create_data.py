# Generated by Django 3.0.5 on 2020-05-01 07:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ideaDetail', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='create_data',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
