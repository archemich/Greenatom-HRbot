from django.contrib import admin
# Register your models here.
from .models import Question, PossibleAnswer

class PossibleAnswerInline(admin.StackedInline):
	model = PossibleAnswer
	extra = 4


class QuestionAdmin(admin.ModelAdmin):
	inlines = [PossibleAnswerInline]
	list_display = ('question_text', 'category', 'difficulty')
	list_filter = ('category', 'difficulty')
	search_fields = ['question_text']









admin.site.register(Question,QuestionAdmin)
