# Generated by Django 5.1.3 on 2024-12-05 04:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='articles',
            new_name='Article',
        ),
    ]
