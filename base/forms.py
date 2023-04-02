# from .models import Profile
# from django import forms
from .models import Student
from django import forms

# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ('hourly_rate', 'time_frames',)

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ("full_name",)