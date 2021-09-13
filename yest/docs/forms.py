from django import forms
from docs.models import StaffModel, ContractModel

trans_zen_han = str.maketrans('ー－０１２３４５６７８９', '--0123456789')

class HankakuNumberField(forms.CharField):
    def clean( self, value):
        return value. translate(trans_zen_han)

class StaffForm(forms.ModelForm):
    class Meta:
        model = StaffModel
        fields = '__all__'
    age=HankakuNumberField()
    tel1=HankakuNumberField()
    tel2=HankakuNumberField()
    fax=HankakuNumberField()


class ContractForm(forms.ModelForm):
    class Meta:
        model = ContractModel
        fields = '__all__'
