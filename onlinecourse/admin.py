from django.contrib import admin
# <HINT> Import any new Models here
from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission

# <HINT> Register QuestionInline and ChoiceInline classes here

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 5 

class QuestionInline(admin.StackedInline):
    model = Question
    extra = 5 

class QuestionAdmin(admin.ModelAdmin):
    model = Question
    list_display = ('course', 'question_text', "grade")
    inlines = [ChoiceInline]

class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5 

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline, QuestionInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']

class SubmissionAdmin(admin.ModelAdmin):
    inlines = [LessonInline, QuestionInline]
    list_display = ('enrollment', 'choices')

class LessonAdmin(admin.ModelAdmin):
    list_display = ['course', 'title']


# <HINT> Register Question and Choice models here

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)

