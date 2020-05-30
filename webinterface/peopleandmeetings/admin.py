from django.contrib import admin
from .models import Person, Meeting


# Register your models here.
class PersonAdmin(admin.ModelAdmin):
    list_display = ('telegram_id', 'tests_score',
                    'competition_score', 'get_prefered_categories')
    search_fields = ['telegram_id']

    def get_prefered_categories(self, obj):
        return ",\n".join([p.category for p in obj.prefered_categories.all()])


class MeetingAdmin(admin.ModelAdmin):
    list_display = ('meeting_name', 'date')
    search_fields = ['meeting_name']


admin.site.register(Person, PersonAdmin)
admin.site.register(Meeting, MeetingAdmin)
