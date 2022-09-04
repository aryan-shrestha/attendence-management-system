from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from account.form import MyUserCreationForm, MyUserUpdateForm
from module.models import Class

# Create your views here.

def loginPage(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        
        else:
            messages.success(request, "Invalid username or password!! ")

    return render(request, 'account/login.html')


def registerTeacher(request):
    
    form = MyUserCreationForm()

    if request.method == "POST":
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = True
            user.save()
            login(request, user)
            messages.success(request, "User registered successfully!")
            return redirect('home')
    
        else:
            messages.error(request, form.errors)

    context = {
        'form': form,
    }
    return render(request, 'account/register.html', context)
    
@login_required(login_url='login')
def registerStudent(request):
    form = MyUserCreationForm()
    classes = Class.objects.all()

    if request.method == "POST":
        form = MyUserCreationForm(request.POST)
        module_id = request.POST.get('class')
        
        if form.is_valid():
            user = form.save()
            class_obj = Class.objects.get(id=module_id)
            class_obj.students.add(user)
            messages.success(request, "User registered successfully!")
            return redirect('home')
    
        else:
            messages.error(request, form.errors)

    context = {
        'form': form,
        'classes': classes,
    }
    return render(request, 'account/register_student.html', context)


def profile(request):
    user = User.objects.get(id=request.user.id)
    form = MyUserUpdateForm(instance=user)

    if request.method == "POST":
        form = MyUserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('home')
        
        else:
            messages.error(request, form.errors)


    context = {
        'form': form
    }

    return render(request, 'account/profile.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')