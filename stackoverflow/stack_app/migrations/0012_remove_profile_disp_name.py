# Generated by Django 3.1.2 on 2020-10-20 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stack_app', '0011_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='disp_name',
        ),
    ]
