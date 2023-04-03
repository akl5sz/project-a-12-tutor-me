from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# Create your models here.

<<<<<<< HEAD
=======
# class Profile(models.Model):
#    name = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.CASCADE
#         )
#    hourly_rate = models.CharField(max_length=40, default="")
#    time_frames = models.CharField(max_length=40, default="")
#    classes = classes = models.TextField(max_length=1000, default="")

#    def __str__(self):
#        return '{} Hourly Rate: {} Time Frames Available: {}'.format(self.name, self.hourly_rate, self.time_frames)

>>>>>>> 244d1d1 (Possible fix migration error)
class Student(models.Model):
    full_name = models.CharField(max_length = 80)
    username = models.CharField(max_length = 80)

    def __str__(self):
        return self.username
    
class Tutor(models.Model):
    username = models.CharField(max_length = 80)
    hourly_rate = models.CharField(max_length = 40)
    time_frames = models.CharField(max_length = 40)
    #Represents the list of courses for a particular tutor (courses the tutor has posted)
    tutor_all_courses = models.ManyToManyField('Course', through = 'CourseTutored')

    def __str__(self):
        return self.username
    
class Course(models.Model):
    mnem = models.CharField(max_length=8) #Example: 'APMA'
    num = models.CharField(max_length = 8, default = "0000") #Example: '3080'
    descr = models.CharField(max_length=200) #Example: 'Linear Algebra'
    #Represents the list of tutors for a particular course (allows students to view tutors for that course)
    course_all_tutors = models.ManyToManyField('Tutor', through = 'CourseTutored')

    def __str__(self):
        return self.mnem + " " + self.num + " " + self.descr

#Django "Through" tables that establishes direct connection between Tutors and Courses
class CourseTutored(models.Model):
    tutor = models.ForeignKey(Tutor, on_delete = models.CASCADE)
    course = models.ForeignKey(Course, on_delete = models.CASCADE)

