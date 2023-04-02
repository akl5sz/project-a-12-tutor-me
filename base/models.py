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

# class Student(models.Model):
#     full_name = models.CharField(max_length = 80)
#     #username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
#     username = User.username
#     def __str__(self):
#         return self.full_name


class Studentss(models.Model):
    #full_name = models.CharField(max_length = 80)
    #username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    username = models.CharField(max_length = 80)
    def __str__(self):
        return self.username

class Tutor(models.Model):
    username = models.CharField(max_length = 80)
    # hourly_rate = models.CharField(max_length = 40)
    # time_frames = models.CharField(max_length = 40)
    def __str__(self):
        return self.username


class Course(models.Model):
    mnem = models.CharField(max_length=8) #Example: 'APMA'
    num = models.CharField(max_length = 8, default = "0000") #Example: '3080'
    descr = models.CharField(max_length=200) #Example: 'Linear Algebra'

    def __str__(self):
        return self.mnem + " " + self.num + " " + self.descr