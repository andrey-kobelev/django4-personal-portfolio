# Generated by Django 4.1.5 on 2023-01-22 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_allblogs'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Blog',
        ),
    ]
