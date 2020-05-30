from django.db import models

# Create your models here.

class Category(models.Model):

    category = models.CharField('Категория', max_length=100)
    isOn = models.BooleanField('Включить категорию', default=True,
                               null=False, blank=False)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['-isOn', 'category']


class Question (models.Model):

    question_text = models.TextField('Текст вопроса', max_length=500)

    true_answer = models.CharField('Правильный ответ', max_length=50,
                                   default='Введите ответ', null=False,
                                   blank=False)

    DIFFICULTY = [
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Hard', 'Hard'),
    ]
    difficulty = models.CharField('Сложность', max_length=50,
                                  choices=DIFFICULTY,
                                  default='Выберите сложность')

    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 verbose_name='Категория')

    def isOn(self):
        a = self.category.isOn
        short_description = 'Включен'
        if a is True:
            return 'Да'
        else:
            return 'Нет'

    def __str__(self):
        return self.question_text[:20]

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class PossibleAnswer (models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE,
                                 verbose_name='Вопрос')

    answer = models.CharField('Ответ', max_length=50)

    def __str__(self):
        return self.answer

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
