from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

# from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login

from .models import CustomerModel, StaffModel
from django.http import HttpResponse

from .forms import StaffForm

# Create your views here.
def customerList(request):
    customer_list = CustomerModel.objects.all()
    return render(request, 'customerlist.html', { 'customer_list':customer_list })

def DocsHiyomeisai(request):  
    customer_list = CustomerModel.objects.all()
    return render(request, 'hiyomeisai.html', { 'customer_list':customer_list })

# 0912
def staff_top(request):
    staff_list = StaffModel.objects.all()
    context = {"staff_list": staff_list}
    return render(request, "staff_top.html", context)

@login_required
def staff_new(request):
    if request.method == 'POST':
        form = StaffForm(request.POST)
        if form.is_valid():
            staff = form.save(commit=False)
            staff.save()
            return redirect(staff_detail, staff_id=staff.pk)
    else:
        form = StaffForm()
    return render(request, "staff_new.html", {'form': form})

@login_required
def staff_edit(request, staff_id):
    staff = get_object_or_404(StaffModel, pk=staff_id)
    # if staff.created_by_id != request.user.id:
    #     return HttpResponseForbidden("このスニペットの編集は許可されていません。")

    if request.method == "POST":
        form = StaffForm(request.POST, instance=staff)
        if form.is_valid():
            form.save()
            return redirect('staff_detail', staff_id=staff_id)
    else:
        form = StaffForm(instance=staff)
    return render(request, 'staff_edit.html', {'form': form})


def staff_detail(request, staff_id):
    staff = get_object_or_404(StaffModel, pk=staff_id)
    return render(request, 'staff_detail.html',
                  {'staff': staff})    