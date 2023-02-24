from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render

from .decorators import allowed_users

def index(request):
    return render(request, 'base/index.html')

def loginPage(request):
    return render(request, 'base/login.html')

@allowed_users(allowed_roles=['student'])
def studentPage(request):
    return render(request, 'base/student.html')

@allowed_users(allowed_roles=['tutor'])
def tutorPage(request):
    return render(request, 'base/tutor.html')
