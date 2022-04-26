from django.shortcuts import render,redirect

# importing Django forms
from django.contrib.auth.forms import UserCreationForm

from django.forms import inlineformset_factory

from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
# handling login,signin and logout
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CreateUserForm
from . decorators import unauthenticated_user,allowed_users
from django.views.decorators.http import require_http_methods


# Create your views here.
# @unauthenticated_user
def signUp(request):
    form = CreateUserForm()

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        post= {
            'username':username,
            'email':email,
            'password1':password1,
            'password2':password2
        }
        form = CreateUserForm(post)
        if form.is_valid(): 
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='student')
            user.groups.add(group)
            # if Group.objects.get('name') == 'student':
            #     return redirect('user-page')

            messages.success(request, 'Account for '+username+' has been created successfully')
            return redirect('login')
        else:
            messages.warning(request,str(form.errors))
            return redirect('account-signUp')
    
    context= { 
        'form':form
    }
    return render(request, 'account/signUp.html',context)

# @unauthenticated_user
# @allowed_users
# @require_http_methods
def logIn(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            group = request.user.groups.all()[0].name
            if group == 'admin':
                return redirect('dashboard-page')
            else:
                return redirect('user-page')
        else:
            messages.info(request, 'wrong credentials')
    context= {}

    return render(request, 'account/login.html',context)


def logOut(request):
    logout(request)
    return redirect('login')

# @login_required(login_url='account-logIn')
# @allowed_users(allowed_roles=['admin'])
# def dashboard(request):
#     return render(request, 'dashboard/dashboard.html')


def index(request):
    return redirect('login')