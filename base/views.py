from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponseRedirect(request, 'index/')