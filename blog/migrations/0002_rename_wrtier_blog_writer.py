# Generated by Django 3.2.2 on 2021-05-18 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='wrtier',
            new_name='writer',
        ),
    ]