# Generated by Django 3.0.6 on 2020-05-30 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='isOn',
            field=models.BooleanField(default=True, verbose_name='Включить категорию'),
        ),
    ]