# Generated by Django 3.0.5 on 2020-10-15 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stack_app', '0004_questions_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='slug',
            field=models.SlugField(),
        ),
    ]
