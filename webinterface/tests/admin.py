from django.contrib import admin
from .models import Question, PossibleAnswer, Category


class PossibleAnswerInline(admin.StackedInline):
    model = PossibleAnswer
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    inlines = [PossibleAnswerInline]
    list_display = ('question_text', 'category', 'difficulty', 'isOn')
    list_filter = ('category', 'difficulty')
    search_fields = ['question_text', 'category']


class CategoryAdmin(admin.ModelAdmin):
    Question.isOn.short_description = 'Включен?'
    list_display = ('category', 'isOn')
    list_editable = ('isOn',)
    list_filter = ('isOn',)
    search_fields = ('category',)

admin.site.register(Question, QuestionAdmin)
admin.site.register(Category, CategoryAdmin)
