from django.contrib import admin

<<<<<<< HEAD
from .models import Course, Student, Tutor, CourseTutored
=======
from .models import Course, Student, Tutor
>>>>>>> 244d1d1 (Possible fix migration error)
#from .models import Profile

# Register your models here.

<<<<<<< HEAD
models = [Course, Student, Tutor, CourseTutored]
=======
models = [Course, Student, Tutor]
>>>>>>> 244d1d1 (Possible fix migration error)
admin.site.register(models)
