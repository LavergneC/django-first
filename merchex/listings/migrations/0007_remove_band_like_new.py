# Generated by Django 4.0.4 on 2022-05-08 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0006_band_like_new'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='band',
            name='like_new',
        ),
    ]
