from django.contrib import admin
# from django.contrib.contenttypes.admin import GenericTabularInline
# Register your models here.
from .models import Post,Theme,Unit,Help,HelpImage,WordTheme
from .models import Word,Tag,TagTheme

class BlogAdmin(admin.ModelAdmin):
    list_display = ["title", "updated", "timestamp"]
    list_display_links = ["updated"]
    list_filter = ["updated", "timestamp"]
    search_fields = ["title"]
    list_editable = ["title"]
    class Meta:
        model = Post

class HelpImageInline(admin.TabularInline):
    model = HelpImage
    extra = 3

class Theme1Inline(admin.TabularInline):
    model = WordTheme
    extra = 3

class ThemeInline(admin.TabularInline):
    model = Theme
    extra = 3

# class TWInline(admin.TabularInline):
#     model = TaskWord
#     extra = 3

class TTInline(admin.TabularInline):
    model = TagTheme
    extra = 3


# class AnswerInline(admin.TabularInline):
#     model = Answer
#     extra = 4

# class TTaInline(admin.TabularInline):
#     model = TaskTheme
#     extra = 4

class UnitAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields': ['type','title','slug','image']}),
        ]
    inlines = [ThemeInline]


class ThemeAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields': ['unit','inner_unit','slug','theme_title','extra_title','image']}),
        ]
    inlines = [TTInline]


class WordAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields': ['kanji','onyomi','kunyomi','translation']}),
        ]
    inlines = [Theme1Inline]

# class TaskAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None,{'fields': ['text', 'num1', 'num2', 'num3', 'num4',
#                           'answer_text1', 'answer_text2', 'answer_text3', 'answer_text4',
#                           'ok1', 'ok2', 'ok3', 'ok4']}),
#         ]
#     inlines = [AnswerInline,TWInline,TTaInline]

class HelpAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['title', 'theme','inner_unit','slug']}),
        ]
    inlines = [HelpImageInline]
    list_display = ('title','inner_unit')

admin.site.register(Help, HelpAdmin)


admin.site.register(Post, BlogAdmin)
admin.site.register(Theme,ThemeAdmin)
admin.site.register(Unit,UnitAdmin)
admin.site.register(Word, WordAdmin)
admin.site.register(Tag)
# admin.site.register(TaskTheme)
# admin.site.register(Task, TaskAdmin)
# admin.site.register(TaskWord)
admin.site.register(TagTheme)

