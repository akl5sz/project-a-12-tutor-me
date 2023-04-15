from django import forms

class TutorLookupForm(forms.Form): #finds the class then finds the tutors associated with that class
    department = forms.CharField(max_length=8) #Example: 'APMA'
    number = forms.CharField(max_length=8) #Example: '3080'
    name = forms.CharField(max_length=200)

class TutorPostCourseForm(forms.Form):
    department = forms.CharField(max_length=8) #Example: 'APMA'
    number = forms.CharField(max_length=8) #Example: '3080'
    name = forms.CharField(max_length=200)

class TutorPostRateForm(forms.Form):
    rate = forms.CharField(max_length = 8)

class TutorRemoveCourseForm(forms.Form):
    department = forms.CharField(max_length=8) #Example: 'APMA'
    number = forms.CharField(max_length=8) #Example: '3080'
    name = forms.CharField(max_length=200)

class StudentRequestTutorForm(forms.Form):
    tutor = forms.CharField(max_length=40)