from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from blogs.models import Post
from django.contrib.auth.decorators import login_required
# Create your views here.

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username,password = password)
            if user is not None:
                login(request,user)
                return redirect('blogs:index')
    else:
        form = AuthenticationForm()

    return render(request,'users/login.html',{'form':form})

def user_logout(request):
    logout(request)
    return redirect('blogs:index')

def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:user_login')
    else:
        form = UserCreationForm()

    return render(request,'users/register.html',{'form':form})
@login_required
def profile(request):
    user = request.user
    posts = Post.objects.filter(owner=user)
    return render(request,'users/profile.html',{'user':user,'posts':posts})