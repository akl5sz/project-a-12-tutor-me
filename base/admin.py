from django.contrib import admin

from .models import Course, Studentss, Tutor
#from .models import Profile

# Register your models here.

models = [Course, Studentss, Tutor]
admin.site.register(models)
