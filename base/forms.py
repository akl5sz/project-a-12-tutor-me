<<<<<<< HEAD
=======
# from .models import Profile
# from django import forms
from .models import Student
from .models import Course

>>>>>>> 244d1d1 (Possible fix migration error)
from django import forms

<<<<<<< HEAD
class TutorLookupForm(forms.Form): #finds the class then finds the tutors associated with that class
=======
# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ('hourly_rate', 'time_frames',)

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

        
class AddCourseForm(forms.Form):
>>>>>>> 244d1d1 (Possible fix migration error)
    mnem = forms.CharField(max_length=8) #Example: 'APMA'
    num = forms.CharField(max_length=8) #Example: '3080'
    descr = forms.CharField(max_length=200)

class TutorPostCourseForm(forms.Form):
    mnem = forms.CharField(max_length=8) #Example: 'APMA'
    num = forms.CharField(max_length=8) #Example: '3080'
    descr = forms.CharField(max_length=200)

class TutorPostRateForm(forms.Form):
    rate = forms.CharField(max_length = 8)

class TutorRemoveCourseForm(forms.Form):
    mnem = forms.CharField(max_length=8) #Example: 'APMA'
    num = forms.CharField(max_length=8) #Example: '3080'
    descr = forms.CharField(max_length=200)