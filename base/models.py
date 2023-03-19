from django.conf import settings
from django.db import models

# Create your models here.

class Profile(models.Model):
    name = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
        )
    hourly_rate = models.CharField(max_length=40)
    time_frames = models.CharField(max_length=40)

    def __str__(self):
        return '{} - {}'.format(self.user, self.classes)

class Course(models.Model):
    mnem = models.CharField(max_length=8) #Example: 'APMA'
    num = models.CharField(max_length = 8, default = "0000") #Example: '3080'
    descr = models.CharField(max_length=200) #Example: 'Linear Algebra'
    def __str__(self):
        return self.mnem + " " + self.num + " " + self.descr