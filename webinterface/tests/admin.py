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
    actions = ['setEasyDif', 'setMedDif', 'setHardDif']

    def setEasyDif(self, request, queryset):
        rows_updated = queryset.update(difficulty='Easy')
        if rows_updated == 1:
            message_bit = '1 вопросу'
        else:
            message_bit = '%s вопросам' % rows_updated
        self.message_user(
            request, "%s установлена сложность \"Easy\"" % message_bit)
    setEasyDif.short_description = 'Установить сложность Easy'

    def setMedDif(self, request, queryset):
        rows_updated = queryset.update(difficulty='Medium')
        if rows_updated == 1:
            message_bit = '1 вопросу'
        else:
            message_bit = '%s вопросам' % rows_updated
        self.message_user(
            request, "%s установлена сложность \"Medium\"" % message_bit)
    setMedDif.short_description = 'Установить сложность Medium'

    def setHardDif(self, request, queryset):
        rows_updated = queryset.update(difficulty='Hard')
        if rows_updated == 1:
            message_bit = '1 вопросу'
        else:
            message_bit = '%s вопросам' % rows_updated
        self.message_user(
            request, "%s установлена сложность \"Hard\"" % message_bit)
    setHardDif.short_description = 'Установить сложность Hard'


class CategoryAdmin(admin.ModelAdmin):
    Question.isOn.short_description = 'Включен?'
    list_display = ('category', 'isOn')
    list_editable = ('isOn',)
    list_filter = ('isOn',)
    search_fields = ('category',)
    actions = ['enableCategory', 'disableCategory']

    def disableCategory(self, request, queryset):
        rows_updated = queryset.update(isOn=False)
        if rows_updated == 1:
            message_bit = '1 категория была'
        elif rows_updated % 10 >= 2 and rows_updated % 10 <= 4:
            message_bit = '%s категории были' % rows_updated
        else:
            message_bit = '%s категорий были' % rows_updated
        self.message_user(request, "%s отключено" % message_bit)
    disableCategory.short_description = 'Отключить категории'

    def enableCategory(self, request, queryset):
        rows_updated = queryset.update(isOn=True)
        if rows_updated == 1:
            message_bit = '1 категория была'
        elif rows_updated % 10 >= 2 and rows_updated % 10 <= 4:
            message_bit = '%s категории были' % rows_updated
        else:
            message_bit = '%s категорий были' % rows_updated
        self.message_user(request, "%s включены" % message_bit)
    enableCategory.short_description = 'Включить категории'


admin.site.register(Question, QuestionAdmin)
admin.site.register(Category, CategoryAdmin)
