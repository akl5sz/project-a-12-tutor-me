from django.contrib import admin

from .models import Course, Student
#from .models import Profile

# Register your models here.

models = [Course, Student]
admin.site.register(models)
