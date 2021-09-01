from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login
from .models import CustomerModel


# Create your views here.
def customerList(request):
    customer_list = CustomerModel.objects.all()
    return render(request, 'customerlist.html', { 'customer_list':customer_list })

def DocsHiyomeisai(request):  
    customer_list = CustomerModel.objects.all()
    return render(request, 'hiyomeisai.html', { 'customer_list':customer_list })