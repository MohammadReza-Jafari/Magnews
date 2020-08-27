# Generated by Django 3.1 on 2020-08-14 01:58

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20200814_0627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main',
            name='link',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='main',
            name='phone_number',
            field=models.CharField(max_length=100, validators=[main.models.phone_number_validator]),
        ),
    ]