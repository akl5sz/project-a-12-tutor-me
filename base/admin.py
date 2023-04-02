from django.contrib import admin

from .models import Course, Students, Tutor
#from .models import Profile

# Register your models here.

models = [Course, Students, Tutor]
admin.site.register(models)
