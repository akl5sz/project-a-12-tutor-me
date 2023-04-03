from django.contrib import admin

from .models import Course, Student, Tutor
#from .models import Profile

# Register your models here.

models = [Course, Student, Tutor]
admin.site.register(models)
