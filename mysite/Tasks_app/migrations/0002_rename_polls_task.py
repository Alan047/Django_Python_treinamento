# Generated by Django 5.0 on 2023-12-17 01:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tasks_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='polls',
            new_name='Task',
        ),
    ]