from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login

# Create your views here.
def signupview(request):
    if request.method == 'POST':
        username_data = request.POST.get('username_data')
        email_data = request.POST.get('email_data')
        password_data = request.POST.get('password_data')
        try:
            user = User.objects.create_user(username_data, email_data, password_data)
        except IntegrityError:
            return render(request, 'signup.html', {'error':'このユーザー名は既に登録されています'})
    else:
        return render(request, 'signup.html', {})
    return render(request, 'signup.html', {'error':username_data+'さんのユーザー登録に成功しました'})

def loginview(request):
    if request.method == 'POST':
        username_data = request.POST.get('username_data')
        password_data = request.POST.get('password_data')
        user = authenticate(request, username=username_data, password=password_data)
        if user is not None:
            login(request, user)
            return redirect('list')
        else:
            return redirect('login')
    return render(request, 'login.html')

