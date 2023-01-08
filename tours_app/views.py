from django.shortcuts import render
from django.http import HttpResponse
from tours_app.models import AccessRecord


# Create your views here.

def index(request):
    # return HttpResponse('Hello World!')
    # data_dict = {'test_data': 'Message from tours_app/views.py'}
    access_records = AccessRecord.objects.order_by('date')
    data_dict = {"access_records": access_records}
    return render(request, 'tours_app/index.html', context=data_dict)


def app_two(request):
    return HttpResponse('<em>Hello World!</em>')


def help(request):
    return render(request, 'tours_app/help.html')


def include_index(request):
    return HttpResponse('<b>Hello World!</b>')
