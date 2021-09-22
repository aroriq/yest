from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

# from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login

from .models import CustomerModel, StaffModel, ContractModel
from django.http import HttpResponse

from .forms import StaffForm, ContractForm, ReceiptForm
from django.views.generic.edit import FormView

# Create your views here.
def customerList(request):
    customer_list = CustomerModel.objects.all()
    return render(request, 'customerlist.html', { 'customer_list':customer_list })

def DocsHiyomeisai(request):  
    customer_list = CustomerModel.objects.all()
    return render(request, 'hiyomeisai.html', { 'customer_list':customer_list })

# staff
@login_required
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
    #     return HttpResponseForbidden("この編集は許可されていません。")

    if request.method == "POST":
        form = StaffForm(request.POST, instance=staff)
        if form.is_valid():
            form.save()
            return redirect('staff_detail', staff_id=staff_id)
    else:
        form = StaffForm(instance=staff)
    return render(request, 'staff_edit.html', {'form': form})

@login_required
def staff_detail(request, staff_id):
    staff = get_object_or_404(StaffModel, pk=staff_id)
    return render(request, 'staff_detail.html',
                  {'staff': staff})    


# contract
@login_required
def contract_top(request):
    contract_list = ContractModel.objects.all()
    context = {"contract_list": contract_list}
    return render(request, "contract_top.html", context)

@login_required
def contract_new(request):
    if request.method == 'POST':
        form = ContractForm(request.POST)
        if form.is_valid():
            contract = form.save(commit=False)
            contract.save()
            return redirect(contract_detail, contract_id=contract.pk)
    else:
        form = ContractForm()
    return render(request, "contract_new.html", {'form': form})

@login_required
def contract_edit(request, contract_id):
    contract = get_object_or_404(ContractModel, pk=contract_id)
    # if contract.created_by_id != request.user.id:
    #     return HttpResponseForbidden("この編集は許可されていません。")

    if request.method == "POST":
        form = ContractForm(request.POST, instance=contract)
        if form.is_valid():
            form.save()
            return redirect('contract_detail', contract_id=contract_id)
    else:
        form = ContractForm(instance=contract)
    return render(request, 'contract_edit.html', {'form': form})

@login_required
def contract_detail(request, contract_id):
    contract = get_object_or_404(ContractModel, pk=contract_id)
    return render(request, 'contract_detail.html',
                  {'contract': contract})

@login_required
def meisai_print(request, contract_id):
    contract = get_object_or_404(ContractModel, pk=contract_id)
    return render(request, 'meisai_print.html',
                  {'contract': contract})

@login_required
def kanrimeisai_print(request, contract_id):
    contract = get_object_or_404(ContractModel, pk=contract_id)
    return render(request, 'kanrimeisai_print.html',
                  {'contract': contract})

@login_required
def zanmu_print(request, contract_id):
    contract = get_object_or_404(ContractModel, pk=contract_id)
    return render(request, 'zanmu_print.html',
                  {'contract': contract})

@login_required
def report_print(request, contract_id):
    contract = get_object_or_404(ContractModel, pk=contract_id)
    return render(request, 'report_print.html',
                  {'contract': contract})


@login_required
def receipt_print(request, contract_id):
    contract = get_object_or_404(ContractModel, pk=contract_id)
    return render(request, 'receipt_print.html',
                  {'contract': contract})

@login_required
def receipt_edit(request, contract_id):
    contract = get_object_or_404(ContractModel, pk=contract_id)

    if request.method == "POST":
        form = ReceiptForm(request.POST, instance=contract)
        if form.is_valid():
            form.save()
            return render(request, 'receipt_print.html',
                 {'contract': contract})
            # return redirect('receipt_print.html', contract_id=contract_id)
    else:
        form = ReceiptForm(instance=contract)
    return render(request, 'receipt_edit.html', {'form': form})

@login_required
def keyreceipt_print(request, contract_id):
    contract = get_object_or_404(ContractModel, pk=contract_id)
    return render(request, 'keyreceipt_print.html',
                  {'contract': contract})

@login_required
def fax_print(request, contract_id):
    contract = get_object_or_404(ContractModel, pk=contract_id)
    return render(request, 'fax_print.html',
                  {'contract': contract})


from django.contrib import messages
from django.views.generic.edit import FormView
from docs.forms import CulcForm
class CulcView(FormView):
    template_name = 'culcform.html'
    form_class = CulcForm
    success_url = 'culc'  # リダイレクト先URL
    def form_valid(self, form):
        form.save()  # 保存処理など
        messages.add_message(self.request, messages.SUCCESS, '登録しました！')  # メッセージ出力
        return super().form_valid(form)