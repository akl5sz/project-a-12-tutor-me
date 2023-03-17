from django.db import models

# Create your models here.
class Course(models.Model):
    descr = models.CharField(max_length=200)
    mnem = models.CharField(max_length=4)
    def __str__(self):
        return self.descr