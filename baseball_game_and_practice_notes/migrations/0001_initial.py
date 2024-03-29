# Generated by Django 2.2.4 on 2019-08-28 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PracticeNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('weather', models.CharField(max_length=10)),
                ('practice_menu', models.TextField(max_length=1000)),
                ('conscious_batting', models.TextField(max_length=1000)),
                ('conscious_defensive', models.TextField(max_length=1000)),
                ('conscious_running', models.TextField(max_length=1000)),
                ('advice', models.TextField(max_length=1000)),
                ('conscious_next', models.TextField(max_length=1000)),
            ],
        ),
    ]
