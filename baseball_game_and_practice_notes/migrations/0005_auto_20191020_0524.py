# Generated by Django 2.2.4 on 2019-10-20 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseball_game_and_practice_notes', '0004_auto_20191020_0517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='practicenote',
            name='advice',
            field=models.TextField(default='特になし', max_length=1000),
        ),
        migrations.AlterField(
            model_name='practicenote',
            name='batting',
            field=models.TextField(default='特になし', max_length=1000),
        ),
        migrations.AlterField(
            model_name='practicenote',
            name='defense',
            field=models.TextField(default='特になし', max_length=1000),
        ),
        migrations.AlterField(
            model_name='practicenote',
            name='running',
            field=models.TextField(default='特になし', max_length=1000),
        ),
    ]