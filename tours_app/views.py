from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from tours_app.models import AccessRecord, User, AuthUser, UserProfileInfo
from . import forms
from tours_app.forms import NewUserForm, UserForm, UserProfileInfoForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View, TemplateView


# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        return {'injectme': 'abc'}


def index(request):
    # return HttpResponse('Hello World!')
    # data_dict = {'test_data': 'Message from tours_app/views.py'}
    # access_records = AccessRecord.objects.order_by('date')
    # data_dict = {"access_records": access_records}
    data_dict = {'message': 'hello world', 'num': 10}
    return render(request, 'tours_app/index.html', context=data_dict)


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


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


def users(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('Error form invalid')
    else:
        form = NewUserForm()

    return render(request, 'tours_app/users.html', {'form': form})


def other(request):
    return render(request, 'tours_app/other.html')


def relative(request):
    return render(request, 'tours_app/relative_url_template.html')


def other(request):
    return render(request, 'tours_app/other.html')


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileInfoForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm
        profile_form = UserProfileInfoForm
    return render(request,
                  'tours_app/registration.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registered': registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account Not Active")
        else:
            print("Someone tired to login and failed")
            print(f"Username: {username} and password: {password}")
            return HttpResponse("Invalid login")
    else:
        return render(request, 'tours_app/login.html')
