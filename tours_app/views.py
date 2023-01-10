from django.shortcuts import render
from django.http import HttpResponse
from tours_app.models import AccessRecord, User
from . import forms


# Create your views here.

def index(request):
    # return HttpResponse('Hello World!')
    # data_dict = {'test_data': 'Message from tours_app/views.py'}
    # access_records = AccessRecord.objects.order_by('date')
    # data_dict = {"access_records": access_records}
    data_dict = {'message': 'hello world', 'num': 10}
    return render(request, 'tours_app/index.html', context=data_dict)


def app_two(request):
    return HttpResponse('<em>Hello World!</em>')


def help(request):
    return render(request, 'tours_app/help.html')


def include_index(request):
    return HttpResponse('<b>Hello World!</b>')


def user_page(request):
    users = User.objects.order_by('first_name')
    data = {'users': users}
    return render(request, 'tours_app/users.html', context=data)


def form_name_view(request):
    if request.method == 'POST':
        form = forms.FormName(request.POST)
        if form.is_valid():
            print(f"Name: {form.cleaned_data['name']}")
            print(f"Email: {form.cleaned_data['email']}")
            print(f"Text: {form.cleaned_data['text']}")
    else:
        form = forms.FormName()
    return render(request, 'tours_app/form_page.html', {'form': form})


def other(request):
    return render(request, 'tours_app/other.html')
