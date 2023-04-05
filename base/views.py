from django.contrib.auth.models import Group

from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render


from .models import Student, Tutor, Course, CourseTutored
from .forms import PostCourseForm, TutorLookupForm, PostRateForm
from .models import User

from .decorators import allowed_users
import base.script
from django.views.generic import  ListView
from django.db.models import Q

def index(request):
    return render(request, 'base/index.html')

def is_student(user):
    return user.groups.filter(name='student').exists()

def is_tutor(user):
    return user.groups.filter(name='tutor').exists()

def loginPage(request):
    if request.user.is_active:
        if not is_student(request.user) and not is_tutor(request.user): #if the logged in user is not a tutor or student, make them register to be one
            return registerPage(request)

    return render(request, 'base/login2.html') #Puts person at the page where they can be recorded as a "user"

def registerPage(request):
    if(request.GET.get('student')): #add student group attribute
        group = Group.objects.get(name='student')
        request.user.groups.add(group)
        group = Group.objects.get(name='tutor')
        request.user.groups.remove(group)
        # return render(request, 'base/student.html')
        return register_student(request)

    elif(request.GET.get('tutor')):
        group = Group.objects.get(name='tutor')
        request.user.groups.add(group)
        group = Group.objects.get(name='student')
        request.user.groups.remove(group)
        # return render(request, 'base/tutor.html')
        return register_tutor(request)
    else:
        return render(request, 'base/register.html')


#Creates student object if needed
def register_student(request):
    user_name = request.user.username
    s = Student(username = user_name)
    s.save()
    return render(request, 'base/student_home.html')

#Creates tutor object if needed
def register_tutor(request):
    user_name = request.user.username
    t = Tutor(username = user_name)
    t.save()
    return render(request, 'base/tutor_home.html')

#Only lets users with "student" group access page
@allowed_users(allowed_roles=['student'])
def studentPage(request):
    return render(request, 'base/student_home.html')

@allowed_users(allowed_roles=['student'])
def studentFindTutor(request):
    if request.method == "POST":
        form = TutorLookupForm(request.POST)
        if form.is_valid():
            mnem = str(form.cleaned_data['mnem']) #first find the right course
            num = str(form.cleaned_data['num'])
            descr = str(form.cleaned_data['descr'])
            if Course.objects.filter(mnem = mnem, num = num, descr = descr).exists(): #Ensures that an incorrect course is not posted
                c = Course.objects.get(mnem = mnem, num = num, descr = descr)
                c.save()
                return render(request, "base/student_tutors_available.html", {'tutors' : c.course_all_tutors.values()}) #now simply use the course and find the tutors
    form = TutorLookupForm()
    return render(request, 'base/student_find_tutor.html', {'form': form})

@allowed_users(allowed_roles=['student'])
def studentTutorSearch(request):
    return render(request, 'base/student_tutors_available.html')

@allowed_users(allowed_roles=['tutor'])
def tutorHome(request):
    return render(request, 'base/tutor_home.html')

#View courses function
@allowed_users(allowed_roles=['tutor'])
def viewCourses(request):
    t = Tutor.objects.get(username = request.user.username)
    return render(request, 'base/tutor_view_courses.html', {'tutor_courses': t.tutor_all_courses.values()})

@allowed_users(allowed_roles=['tutor'])
def postCourses(request):
    # url = "https://sisuva.admin.virginia.edu/psc/ihprd/UVSS/SA/s/WEBLIB_HCX_CM.H_CLASS_SEARCH.FieldFormula." \
    #       "IScript_ClassSearch?institution=UVA01&page=1"
    # response = base.script.url([('term', '1228')])
    # response = base.script.url([('page', 4)])
    # return render(request, 'base/courses.html', {'response' : response})

    #Posting course functionality, problem is that same course can be posted multiple times
    if request.method == "POST":
        form = PostCourseForm(request.POST)
        if form.is_valid():
            t = Tutor.objects.get(username = request.user.username) #find the right tutor model
            t.save()
            mnem = str(form.cleaned_data['mnem'])
            num = str(form.cleaned_data['num'])
            descr = str(form.cleaned_data['descr'])
            if Course.objects.filter(mnem = mnem, num = num, descr = descr).exists(): #Ensures that an incorrect course is not posted
                c = Course.objects.get(mnem = mnem, num = num, descr = descr)
                c.save()
                if not CourseTutored.objects.filter(tutor = t, course = c).exists(): #Ensures that we don't add duplicate Course-Tutor relationship
                    CourseTutored(tutor = t, course = c).save() #adds course to tutor object and adds tutor to course object
                return viewCourses(request)
    form = PostCourseForm()
    return render(request, 'base/tutor_post_courses.html', {'form': form})

#TO:DO
#Ability to remove tutor's courses 




#Hourly rate functions

@allowed_users(allowed_roles=['tutor'])
def postRate(request):
    if request.method == "POST":
        form = PostRateForm(request.POST)
        if form.is_valid():
            t = Tutor.objects.get(username = request.user.username) #find the right tutor model
            t.save()
            hr = str(form.cleaned_data['rate'])
            t.hourly_rate = hr
            t.save()
            return viewRate(request)
    form = PostRateForm()
    return render(request, 'base/tutor_post_rate.html', {'form': form})


@allowed_users(allowed_roles=['tutor'])
def viewRate(request):
    t = Tutor.objects.get(username = request.user.username) #find the right tutor model

    return render(request, 'base/tutor_view_rate.html', {'rate': t.hourly_rate})


def courseLookup(request):
    courses = Course.objects.all() #Used to populate courses in auto-drop down bar when Tutor searches for courses
    return render(request, 'base/course_searching.html', {'courses' : courses})
    
# def addCourse(request):
#     # if request.method == 'POST':
#     #     form = AddCourseForm(request.POST)      
#     return render(request)

