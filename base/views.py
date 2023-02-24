from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'base/index.html')

def loginPage(request):
    return render(request, 'base/login.html')

def studentPage(request):
    return render(request, 'base/student.html')

def tutorPage(request):
    return render(request, 'base/tutor.html')
