# Generated by Django 3.1 on 2020-08-21 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subcategory', '0001_initial'),
        ('news', '0004_auto_20200817_1218'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='category_id',
        ),
        migrations.RemoveField(
            model_name='news',
            name='category_name',
        ),
        migrations.AddField(
            model_name='news',
            name='subcategory',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='subcategory.subcategory'),
        ),
    ]