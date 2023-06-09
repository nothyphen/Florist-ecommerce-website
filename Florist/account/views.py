from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Permission

# Create your views here.
def login_web(request):
    try:
        if request.user.is_authenticated:
            return redirect('/')
        else:
            if request.method ==  "POST":
                username = request.POST['username']
                password = request.POST['password']
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('/')
                else:
                    return redirect('/account/login/')
            template_name = 'login.html'
            return render(request, template_name)
    except:
        return render(request, '404.html')

def logout_web(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/')
    else:
        return render(request, '404.html')

def register(request):
    if request.user.is_authenticated:
        return render(request, '404.html')
    else:
        try:
            if request.method == "POST":
                user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
                user.save()
                return redirect('/account/login')
        except :
            template_name = '404.html'
            return render(request, template_name)
    template_name = 'signin.html'
    return render(request, template_name)