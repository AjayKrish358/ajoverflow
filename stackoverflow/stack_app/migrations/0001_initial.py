# Generated by Django 3.0.5 on 2020-10-10 05:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('username', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('ques_id', models.AutoField(primary_key=True, serialize=False)),
                ('question', models.CharField(max_length=500)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stack_app.Users')),
            ],
        ),
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upvote', models.IntegerField(default=0)),
                ('downvote', models.IntegerField(default=0)),
                ('ques_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stack_app.Questions')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stack_app.Users')),
            ],
        ),
    ]
