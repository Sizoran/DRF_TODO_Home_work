# Generated by Django 4.0.4 on 2022-05-29 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_todo_hiden'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='hiden',
            new_name='is_active',
        ),
    ]