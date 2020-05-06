from django.db import models

# Create your models here.




class Question (models.Model):
	
	def category_default():
	    return 'C++'

	question_text = models.TextField('Текст вопроса')
	answer_text = models.CharField('Ответ', max_length = 100, null = True)
	TEST_CATEGORY = [
        ('Java', 'Java'),
        ('C++', 'C++'),
	]
	category = models.CharField('Категории', max_length = 100, 
		choices = TEST_CATEGORY, default = category_default())

	class Meta:
		verbose_name = 'Вопрос'
		verbose_name_plural = 'Вопросы'

