from django.urls import path
from .views import signupview, loginview

urlpatterns = [
    path('', loginview, name='login'),
    path('signup/', signupview, name='signup'),
    path('login/', loginview, name='login'),
]