from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from django.template import loader
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import *
from .forms import *
from .decorator import unauthorized_user, allowed_users, admin_only





ff="usersF"
ml="malonlin_theme"




# register user

def register(request):
    if request.method=='POST':
        form=UserRegister(request.POST)
        if form.is_valid():
            theUser=form.save()
            theUsername=form.cleaned_data.get('username')

            group= Group.objects.get(name='customer')
            theUser.groups.add(group)

            messages.success(request, f'account created, you can login')
            return redirect('login')

    else:
        form= UserRegister()
       
    return render(request, f'{ff}/register.html', {'form':form })


@login_required()
@allowed_users(allowed_roles=['customer'])
def profile(request):
    return render(request, f'{ff}/view1.html')




def loginPage(request):

    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')


        theUser=authenticate(request, username=username, password=password)

        if theUser is not None:

            login(request, theUser)
            return redirect(f'{ff}/view1.html')
        else:
            messages.info(request, 'username or Password doesn\'t match')

    context={

    }
    return render(request, f'{ff}/view1.html', context)



def logoutUser(request):
    logout(request)

    return redirect('login')

#appliction form ID
def createApplication(request):
    form = idApplicationForm()
    form2 = passportApplicationForm()
    if request.method == 'POST':
        form = idApplicationForm(request.POST)
        form2 = passportApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect

    
    context = {'form': form}
    return render(request, '/', context)


