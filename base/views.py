from django.contrib.auth.models import Group

from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render


from .models import Student, Tutor, Course, CourseTutored
from .forms import PostCourseForm
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
    return render(request, 'base/student.html')

#Creates tutor object if needed
def register_tutor(request):
    user_name = request.user.username
    t = Tutor(username = user_name)
    t.save()
    return render(request, 'base/tutor.html')

#Only lets users with "student" group access page
@allowed_users(allowed_roles=['student'])
def studentPage(request):
    return render(request, 'base/student.html')

#Only lets users with "tutor" group access page
@allowed_users(allowed_roles=['tutor'])
def tutorPage(request):
    t = Tutor.objects.get(username = request.user.username)

    tutor_courses = t.tutor_all_courses.values()
    return render(request, 'base/tutor.html', {'tutor_courses': tutor_courses})

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
            c = Course.objects.get(mnem = mnem, num = num, descr = descr)
            c.save()
            CourseTutored(tutor = t, course = c).save() #adds course to tutor object and adds tutor to course object
            return render(request, "base/tutor.html", {'tutor_classes' : t.tutor_all_courses.values()})
    form = PostCourseForm()
    return render(request, 'base/course_posting.html', {'form': form})


@allowed_users(allowed_roles=['tutor'])
def courseLookup(request):
    courses = Course.objects.all() #Used to populate courses in auto-drop down bar when Tutor searches for courses
    return render(request, 'base/course_searching.html', {'courses' : courses})

    
# def addCourse(request):
#     # if request.method == 'POST':
#     #     form = AddCourseForm(request.POST)      
#     return render(request)

