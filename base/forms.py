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

class TutorNotificationForm(forms.Form):
    info = forms.CharField(max_length=1)
    student = forms.CharField(max_length=40)
    course = forms.CharField(max_length=80)

class StudentNotificationForm(forms.Form):
    info = forms.CharField(max_length=1)
    tutor = forms.CharField(max_length=40)
    course = forms.CharField(max_length=80)

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeFrameForm(forms.Form):
    date = forms.DateField(widget= DateInput)
    start_time = forms.TimeField()
    end_time = forms.TimeField()