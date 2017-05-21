from django.contrib import admin

from .models import Task, Choice, TagTask, UserTask


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4

class ThemeInline(admin.TabularInline):
    model = TagTask
    extra = 4

class UserInline(admin.TabularInline):
    model = UserTask
    extra = 4

class TaskAdmin(admin.ModelAdmin):
    # list_display = ['use']
    fieldsets = [
        (None,{'fields': ['text','image']}),
        ]
    inlines = [ChoiceInline,ThemeInline, UserInline]





admin.site.register(Task, TaskAdmin)
admin.site.register(TagTask)
