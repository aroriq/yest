from django.urls import path
from .views import signupview, loginview, logoutview, indexview
from . import views

# app_name = 'yhauth'

urlpatterns = [
    # path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', loginview, name='login'),
    path('logout/', logoutview, name='logout'),
    path('signup/', signupview, name='signup'),
    path('index/', indexview, name='index'),
    path('', loginview, name='login'),
]