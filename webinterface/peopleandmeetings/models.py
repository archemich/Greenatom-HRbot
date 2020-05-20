from django.db import models

# Create your models here.

class Meeting(models.Model):
	meeting_name = models.CharField('Название встречи', max_length = 100)

	date = models.DateField('Дата проведения') 


	class Meta():
		verbose_name = 'Встреча'
		verbose_name_plural = 'Встречи'





class Person(models.Model):
	telegram_id = models.CharField('Telegram Id', max_length = 100, null = False)
	tests_score = models.IntegerField('Очки тестирования', default = 0)
	competion_score = models.IntegerField('Очки соревнования', default = 0)
	visited_meetings = models.ManyToManyField(Meeting, related_name = 'people')


	class Meta():
		verbose_name = 'Человек'
		verbose_name_plural = 'Люди'