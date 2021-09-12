from django import forms
from docs.models import StaffModel

trans_zen_han = str.maketrans('ー－０１２３４５６７８９', '--0123456789')

class HankakuPhoneNumberField(forms.CharField):
    def clean( self, value):
        return value. translate(trans_zen_han)

class StaffForm(forms.ModelForm):
    class Meta:
        model = StaffModel
        fields = '__all__'
    tel1=HankakuPhoneNumberField()
    tel2=HankakuPhoneNumberField()