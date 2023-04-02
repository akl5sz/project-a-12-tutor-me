from django.contrib.auth.models import Group

from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render

#from.models import Profile
from .models import Studentss, Tutor, Course
#from .forms import StudentForm
#from .forms import ProfileForm
from .forms import AddCourseForm
from .models import User

from .decorators import allowed_users
import base.script
from django.views.generic import TemplateView, ListView
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



def register_student(request):
    user_name = request.user.username
    s = Studentss(username = user_name)
    s.save()
    return render(request, 'base/student.html')

def register_tutor(request):
    user_name = request.user.username
    t = Tutor(username = user_name)
    t.save()
    return render(request, 'base/tutor.html')

@allowed_users(allowed_roles=['student'])
def studentPage(request):
    return render(request, 'base/student.html')


@allowed_users(allowed_roles=['tutor'])
def tutorPage(request):
    # if request.method == 'POST':
    #     form = ProfileForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect('base/tutor.html')
        
    # form = ProfileForm()
    return render(request, 'base/tutor.html')


def coursePage(request):
    # url = "https://sisuva.admin.virginia.edu/psc/ihprd/UVSS/SA/s/WEBLIB_HCX_CM.H_CLASS_SEARCH.FieldFormula." \
    #       "IScript_ClassSearch?institution=UVA01&page=1"
    #response = base.script.url([('term', '1228')])
    # response = base.script.url([('page', 4)])
    # return render(request, 'base/courses.html', {'response' : response})
    return render(request, 'base/courses.html')


class SearchResultsView(ListView):
    model = Course
    template_name = 'base/search_results.html'
    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        object_list = Course.objects.filter(
            Q(mnem=query) | Q(num = query) | Q(descr = query)
        )
        return object_list
    
def addCourse(request):
    # if request.method == 'POST':
    #     form = AddCourseForm(request.POST)
        

    return render(request)
        

