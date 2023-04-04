from django.contrib import admin

from .models import Course, Student, Tutor, CourseTutored
#from .models import Profile

# Register your models here.

models = [Course, Student, Tutor, CourseTutored]
admin.site.register(models)
