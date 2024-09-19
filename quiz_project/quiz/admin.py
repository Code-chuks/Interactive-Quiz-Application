# quiz/admin.py
from django.contrib import admin
from .models import Quiz, Question, Answer

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]

class QuizAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
