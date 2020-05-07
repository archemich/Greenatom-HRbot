from django.db import models

# Create your models here.




class Question (models.Model):
	
	question_text = models.TextField('Текст вопроса')

	true_answer = models.CharField('Правильный ответ', max_length = 50, default = 'Введите ответ', null = False, blank = False)


	DIFFICULTY = [
	    ('Easy','Easy'),
	    ('Medium', 'Medium'),
	    ('Hard', 'Hard'),
	]
	difficulty = models.CharField('Сложность', max_length = 50,
		choices = DIFFICULTY, default = 'Выберите сложность')


	CATEGORY = [
		('Java', 'Java'),
		('C++', 'C++'),
	]

	category = models.CharField('Категория', max_length = 100, 
		choices = CATEGORY, default = 'Выберите тему')


	class Meta:
		verbose_name = 'Вопрос'
		verbose_name_plural = 'Вопросы'





class PossibleAnswer (models.Model):
	question = models.ForeignKey(Question,
		on_delete = models.CASCADE)

	answer = models.CharField('Ответ', max_length = 50)

	class Meta:
		verbose_name = 'Ответ'
		verbose_name_plural = 'Ответы'