# Generated by Django 2.2.11 on 2020-03-28 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='image',
            new_name='imageFun',
        ),
    ]
