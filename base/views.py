from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render


def loginPage(request):
    return render(request, 'base/login.html')


def index(request):
    return render(request, 'base/index.html')
