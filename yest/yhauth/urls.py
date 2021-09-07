from django.urls import path
from .views import signupview, loginview
from . import views

# app_name = 'yhauth'

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('', loginview, name='login'),
    path('signup/', signupview, name='signup'),
    path('login/', loginview, name='login'),
]