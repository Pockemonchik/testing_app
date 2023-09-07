from django.contrib import admin
from nested_inline.admin import NestedStackedInline, NestedModelAdmin

from .models import *

class AnswersInline(NestedStackedInline):
    model = Answers
    extra = 3
    fk_name = 'question'

class QuestionInline(NestedStackedInline):
    model = Question
    extra = 3
    fk_name = 'test'
    inlines = [AnswersInline]



class TestingAdmin(NestedModelAdmin):
    model = Test
    inlines = [
        QuestionInline,
    ]

admin.site.register(Test, TestingAdmin)
admin.site.register(Question)
admin.site.register(Answers)

# Register your models here.
