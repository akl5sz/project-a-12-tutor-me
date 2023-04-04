# from .models import Profile
# from django import forms
from .models import Student
from .models import Course
from django.forms import ModelForm
from django import forms
from django.db.models.functions import Concat
from django.db.models import Value as V
from django.forms import Textarea
# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ('hourly_rate', 'time_frames',)

# class StudentForm(forms.ModelForm):
#     class Meta:
#         model = Student
#         fields = '__all__'

        
class PostCourseForm(forms.Form):
    mnem = forms.CharField(max_length=8) #Example: 'APMA'
    num = forms.CharField(max_length=8) #Example: '3080'
    descr = forms.CharField(max_length=200)

