# Generated by Django 3.0.6 on 2020-05-30 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tests', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meeting_name', models.CharField(max_length=100, verbose_name='Название встречи')),
                ('date', models.DateField(verbose_name='Дата проведения')),
            ],
            options={
                'verbose_name': 'Встреча',
                'verbose_name_plural': 'Встречи',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telegram_id', models.CharField(max_length=100, verbose_name='Telegram ID')),
                ('tests_score', models.IntegerField(default=0, verbose_name='Очки тестирования')),
                ('competition_score', models.IntegerField(default=0, verbose_name='Очки соревнования')),
                ('sum_score', models.IntegerField(default=0, editable=False, verbose_name='Суммарные очки')),
                ('prefered_categories', models.ManyToManyField(related_name='prefered_category', to='tests.Category', verbose_name='Предпочитаемые категории')),
                ('visited_meetings', models.ManyToManyField(related_name='people', to='peopleandmeetings.Meeting', verbose_name='Посещенные встречи')),
            ],
            options={
                'verbose_name': 'Человек',
                'verbose_name_plural': 'Люди',
                'ordering': ['-sum_score', '-competition_score'],
            },
        ),
    ]
