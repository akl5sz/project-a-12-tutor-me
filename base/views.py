from django.contrib.auth.models import Group
from django.shortcuts import render
from django.contrib.auth import login as logins, logout as logouts

from .models import Student, Tutor, Course, CourseTutored
from .forms import TutorPostCourseForm, TutorLookupForm, TutorPostRateForm, TutorRemoveCourseForm

from .decorators import allowed_users

def index(request):
    return render(request, 'base/index.html')

def is_student(user):
    return user.groups.filter(name='student').exists()

def is_tutor(user):
    return user.groups.filter(name='tutor').exists()

#-------------------------------------------------------

def loginPage(request):
    if request.user.is_active:
        if not is_student(request.user) and not is_tutor(request.user): #if the logged in user is not a tutor or student, make them register to be one
            return registerPage(request)
        if is_student(request.user):
            return studentHome(request)
        if is_tutor(request.user):
            return tutorHome(request)
    return render(request, 'base/general_login.html') #Puts person at the page where they can be recorded as a "user"

def logout(request):
    if request.method == "POST":
        logouts(request)
        return render(request, 'base/index.html')
    return render(request, 'base/general_logout.html')

def registerPage(request):
    if(request.GET.get('student')): #add student group attribute
        group = Group.objects.get(name='student')
        request.user.groups.add(group)
        group = Group.objects.get(name='tutor')
        request.user.groups.remove(group)
        return register_student(request)
    elif(request.GET.get('tutor')): #add tutor group attribute
        group = Group.objects.get(name='tutor')
        request.user.groups.add(group)
        group = Group.objects.get(name='student')
        request.user.groups.remove(group)
        return register_tutor(request)
    else:
        return render(request, 'base/register.html')
#-------------------------------------------------

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


#------------------------------------------------

#Only lets users with "student" group access page
@allowed_users(allowed_roles=['student'])
def studentHome(request):
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
                return render(request, "base/student_tutors_available.html", {'tutors' : c.course_all_tutors.values()}) #now simply use the course and find the tutors
    form = TutorLookupForm()
    return render(request, 'base/student_find_tutor.html', {'form': form})

@allowed_users(allowed_roles=['student'])
def studentTutorSearch(request):
    return render(request, 'base/student_tutors_available.html')

def studentSubmitRequest(request):
    return render(request, 'base/student_submit_request.html')
#-----------------------------------------------

@allowed_users(allowed_roles=['tutor'])
def tutorHome(request):
    return render(request, 'base/tutor_home.html')

#View courses function
@allowed_users(allowed_roles=['tutor'])
def tutorViewCourses(request):
    t = Tutor.objects.get(username = request.user.username)
    return render(request, 'base/tutor_view_courses.html', {'tutor_courses': t.tutor_all_courses.values()})

@allowed_users(allowed_roles=['tutor'])
def tutorPostCourses(request):
    if request.method == "POST":
        form = TutorPostCourseForm(request.POST)
        if form.is_valid():
            t = Tutor.objects.get(username = request.user.username) #find the right tutor model
            mnem = str(form.cleaned_data['mnem'])
            num = str(form.cleaned_data['num'])
            descr = str(form.cleaned_data['descr'])
            if Course.objects.filter(mnem = mnem, num = num, descr = descr).exists(): #Ensures that an incorrect course is not posted
                c = Course.objects.get(mnem = mnem, num = num, descr = descr)
                if not CourseTutored.objects.filter(tutor = t, course = c).exists(): #Ensures that we don't add duplicate Course-Tutor relationship
                    CourseTutored(tutor = t, course = c).save() #adds course to tutor object and adds tutor to course object
                return tutorViewCourses(request)
    form = TutorPostCourseForm()
    return render(request, 'base/tutor_post_course.html', {'form': form})

def tutorRemoveCourses(request):
    if request.method == "POST":
        form = TutorRemoveCourseForm(request.POST)
        if form.is_valid():
            t = Tutor.objects.get(username = request.user.username) #find the right tutor model
            mnem = str(form.cleaned_data['mnem'])
            num = str(form.cleaned_data['num'])
            descr = str(form.cleaned_data['descr'])
            if Course.objects.filter(mnem = mnem, num = num, descr = descr).exists(): #Ensures that an incorrect course is not posted
                c = Course.objects.get(mnem = mnem, num = num, descr = descr)
                CourseTutored.objects.filter(tutor = t, course = c).delete()
                return tutorViewCourses(request)
    form = TutorRemoveCourseForm()
    return render(request, 'base/tutor_remove_course.html', {'form': form})

#Hourly rate functions

@allowed_users(allowed_roles=['tutor'])
def tutorPostRate(request):
    if request.method == "POST":
        form = TutorPostRateForm(request.POST)
        if form.is_valid():
            t = Tutor.objects.get(username = request.user.username) #find the right tutor model
            hr = str(form.cleaned_data['rate'])
            t.hourly_rate = hr
            t
            return tutorViewRate(request)
    form = TutorPostRateForm()
    return render(request, 'base/tutor_post_rate.html', {'form': form})


@allowed_users(allowed_roles=['tutor'])
def tutorViewRate(request):
    t = Tutor.objects.get(username = request.user.username) #find the right tutor model

    return render(request, 'base/tutor_view_rate.html', {'rate': t.hourly_rate})

#-------------------------------------------------------------------------------

def studentCourseLookup(request):
    courses = Course.objects.all() #Used to populate courses in auto-drop down bar when Student searches for courses
    return render(request, 'base/student_course_lookup.html', {'courses' : courses})

def tutorCourseLookup(request):
    courses = Course.objects.all() #Used to populate courses in auto-drop down bar when Tutor searches for courses
    return render(request, 'base/tutor_course_lookup.html', {'courses' : courses})
    
