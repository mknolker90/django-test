from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from AppTwo.models import User
from AppTwo.forms import UserForm, UserProfileInfoForm
from . import forms

from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout, authenticate
# Create your views here.

def index(request):
    #return HttpResponse("<em>Hello World!</em>")
    context_dict={'text':'hello world','number':100}
    return render(request, 'AppTwo/index.html', context=context_dict)

@login_required
def user_logout(request):
    #return HttpResponse("<em>Hello World!</em>")
    logout(request)
    return HttpResponseRedirect(reverse('index'))




def register(request):
    registered=False
    #return HttpResponse("<em>Hello World!</em>")

    if request.method=='POST':
        user_form=UserForm(data=request.POST)
        profile_form=UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user=user_form.save()
            user.set_password(user.password)
            user.save()

            profile=profile_form.save(commit=False)
            profile.user=user

            if 'profile_pic' in request.FILES:
                profile.profile_pic=request.FILES['profile_pic']

            profile.save()
            registered=True
        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form=UserForm()
        profile_form=UserProfileInfoForm()

    return render(request, 'AppTwo/registration.html',
    context={'user_form': user_form, 'profile_form': profile_form, 'registered': registered})


def form_name_view(request):
    form=forms.FormName()
    if request.method == 'POST':
        form=forms.FormName(request.POST)

        if form.is_valid():
            print ("VALIDATION success")
            print ("NAME :"+ form.cleaned_data['name'])
            print ("Email: "+form.cleaned_data['email'])
            print ("text: "+ form.cleaned_data['text'])

    return render(request, 'AppTwo/form_page.html', context={'form':form})

def users(request):

    form=NewUserForm()
    if request.method=='POST':
        form= NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print ('error')
    return render(request, 'AppTwo/users.html',{'form':form})

def base(request):
    #return HttpResponse("<em>Hello World!</em>")
    return render(request, 'AppTwo/base.html')

def users_old(request):
    user_list=User.objects.order_by('first_name')
    user_dict={'users':user_list}
    return render(request, 'AppTwo/users.html', context=user_dict)


def help(request):
    help_dict={'help_insert':'Help me please file'}
    return render(request, 'AppTwo/help.html', context=help_dict)


def user_login(request):

    if request.method=='POST':

        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username, password=password)

        if user:

            if user.is_active:
                login(request, user)
                print ('successful')
                return HttpResponseRedirect(reverse('index'))
            else:
                print ('not successful')
                return HttpResponse('account not active')
        else:
            print ('some tried in and failed')
            return HttpResponse('invalid reposne')
    else:
        return render(request, 'AppTwo/login.html',{})
