# Generated by Django 3.0.6 on 2020-05-07 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peopleandmeetings', '0002_auto_20200507_1006'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='visited_meetgins',
        ),
        migrations.AddField(
            model_name='person',
            name='visited_meetings',
            field=models.ManyToManyField(related_name='people', to='peopleandmeetings.Meeting'),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='date',
            field=models.DateField(verbose_name='Дата проведения'),
        ),
        migrations.AlterField(
            model_name='person',
            name='competion_score',
            field=models.IntegerField(default=0, verbose_name='Очки соревнования'),
        ),
        migrations.AlterField(
            model_name='person',
            name='tests_score',
            field=models.IntegerField(default=0, verbose_name='Очки тестирования'),
        ),
    ]