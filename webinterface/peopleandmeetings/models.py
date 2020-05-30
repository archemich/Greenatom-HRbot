from tests.models import Category
from django.db import models


# Create your models here.
class Meeting(models.Model):
    meeting_name = models.CharField('Название встречи', max_length=100)
    date = models.DateField('Дата проведения')

    def __str__(self):
        return self.meeting_name

    class Meta():
        ordering = ['meeting_name', '-date']
        verbose_name = 'Встреча'
        verbose_name_plural = 'Встречи'


class Person(models.Model):
    telegram_id = models.CharField('Telegram ID', max_length=100, null=False)
    tests_score = models.IntegerField('Очки тестирования', default=0)
    competition_score = models.IntegerField('Очки соревнования', default=0)
    visited_meetings = models.ManyToManyField(Meeting, related_name='people',verbose_name='Посещенные встречи')
    prefered_categories = models.ManyToManyField(
        Category, related_name='prefered_category',
        verbose_name='Предпочитаемые категории'
    )

    def __str__(self):
        return self.telegram_id

    class Meta():
        verbose_name = 'Человек'
        verbose_name_plural = 'Люди'
        ordering = ['-competition_score', '-tests_score']
