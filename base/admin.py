from django.contrib import admin

from .models import Course, Students, Tutor, Profile
#from .models import Profile

# Register your models here.

models = [Course, Students, Tutor, Profile]
admin.site.register(models)
