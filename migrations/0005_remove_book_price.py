# Generated by Django 3.0.8 on 2020-08-11 06:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20200811_0140'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='price',
        ),
    ]
