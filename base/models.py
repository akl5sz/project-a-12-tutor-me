from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class Profile(models.Model):
#     name = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.CASCADE
#         )
#     hourly_rate = models.CharField(max_length=40)
#     time_frames = models.CharField(max_length=40)

#     def __str__(self):
#         return '{} Hourly Rate: {} Time Frames Available: {}'.format(self.name, self.hourly_rate, self.time_frames)

class Student(models.Model):
    first_name = models.CharField(max_length = 60) #new user must enter this info when they register as a student
    last_name = models.CharField(max_length = 60) #^
    username = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.first_name + " " + self.last_name





class Course(models.Model):
    mnem = models.CharField(max_length=8) #Example: 'APMA'
    num = models.CharField(max_length = 8, default = "0000") #Example: '3080'
    descr = models.CharField(max_length=200) #Example: 'Linear Algebra'

    def __str__(self):
        return self.mnem + " " + self.num + " " + self.descr