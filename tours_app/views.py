from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return HttpResponse('Hello World!')


def app_two(request):
    return HttpResponse('<em>Hello World!</em>')


def include_index(request):
    return HttpResponse('<b>Hello World!</b>')
