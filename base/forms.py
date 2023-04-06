from django import forms

class TutorLookupForm(forms.Form): #finds the class then finds the tutors associated with that class
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