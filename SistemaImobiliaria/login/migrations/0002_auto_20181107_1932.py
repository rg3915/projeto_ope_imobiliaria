# Generated by Django 2.1.2 on 2018-11-07 21:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Pessoa',
            new_name='Usuario',
        ),
    ]
