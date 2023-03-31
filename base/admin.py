from django.contrib import admin

from .models import Course
from .models import Profile

# Register your models here.
models = [Course, Profile]
admin.site.register(models)
