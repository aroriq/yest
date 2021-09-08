from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

# Create your views here.

@login_required
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
            return render(request, 'index.html', {'error':username_data+'さん、ログインに成功しました'})
        else:
            return render(request, 'login.html', {'error':'ログインに失敗しました。ユーザー名とパスワードを確認して下さい。'})
    return render(request, 'login.html', {})

def logoutview(request):
    logout(request)
    # return redirect('login')
    return render(request, 'logout.html', {})


def indexview(request):
    return render(request, 'index.html', {})



# class SignUpView(CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'signup.html'