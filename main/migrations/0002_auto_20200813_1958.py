# Generated by Django 3.1 on 2020-08-13 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='main',
            name='facebook',
            field=models.TextField(default='-'),
        ),
        migrations.AddField(
            model_name='main',
            name='twitter',
            field=models.TextField(default='-'),
        ),
        migrations.AddField(
            model_name='main',
            name='youtube',
            field=models.TextField(default='-'),
        ),
    ]
