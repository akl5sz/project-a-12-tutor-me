from django.contrib import admin

from .models import Course, Student, Tutor, CourseTutored, Notification
#from .models import Profile

# Register your models here.

models = [Course, Student, Tutor, CourseTutored, Notification]
admin.site.register(models)
