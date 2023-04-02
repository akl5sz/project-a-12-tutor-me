# from .models import Profile
# from django import forms
from .models import Students
from django import forms

# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ('hourly_rate', 'time_frames',)

class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        #fields = ("full_name",)