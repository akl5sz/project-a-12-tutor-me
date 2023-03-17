from django.contrib.auth.models import Group

from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render

from .decorators import allowed_users
import base.script

def index(request):
    return render(request, 'base/index.html')

def loginPage(request):

    if(request.GET.get('student')):
        group = Group.objects.get(name='student')
        request.user.groups.add(group)
        group = Group.objects.get(name='tutor')
        request.user.groups.remove(group)
        return render(request, 'base/student.html')

    if(request.GET.get('tutor')):
        group = Group.objects.get(name='tutor')
        request.user.groups.add(group)
        group = Group.objects.get(name='student')
        request.user.groups.remove(group)
        return render(request, 'base/tutor.html')

    return render(request, 'base/login.html')

@allowed_users(allowed_roles=['student'])
def studentPage(request):
    return render(request, 'base/student.html')


@allowed_users(allowed_roles=['tutor'])
def tutorPage(request):
    return render(request, 'base/tutor.html')


def coursePage(request):
    # url = "https://sisuva.admin.virginia.edu/psc/ihprd/UVSS/SA/s/WEBLIB_HCX_CM.H_CLASS_SEARCH.FieldFormula." \
    #       "IScript_ClassSearch?institution=UVA01&page=1"
    response = base.script.url([('page', 1)])
    return render(request, 'base/courses.html', {'response' : response})
