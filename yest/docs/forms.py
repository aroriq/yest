from django import forms
from docs.models import  ContractModel, Post  #StaffModel,

trans_zen_han = str.maketrans('ー－０１２３４５６７８９', '--0123456789')

class HankakuNumberField(forms.CharField):
    def clean( self, value):
        return value. translate(trans_zen_han)

# class StaffForm(forms.ModelForm):
#     class Meta:
#         model = StaffModel
#         fields = '__all__'
#     age=HankakuNumberField()
#     tel1=HankakuNumberField()
#     tel2=HankakuNumberField()
#     fax=HankakuNumberField()


class ContractForm(forms.ModelForm):
    class Meta:
        model = ContractModel
        fields = '__all__'

class ReceiptForm(forms.ModelForm):
    class Meta:
        model = ContractModel
        fields = ('receipt_atena', 'receipt_meimo', 'receipt_total', 'receiptremarks1')
        labels = {
            'receipt_atena': '宛名',
            'receipt_meimo': '但し書き',
            'receipt_total': '合計金額',
            'receiptremarks1': '備考'
        }
        help_texts = {
            'receipt_atena': '様',
            'receipt_meimo': 'として',
            'receipt_total': '円',
            'receiptremarks1': ''
        }


from django.forms import forms, CharField
# from docs.models import Post
class CulcForm(forms.Form):
    title = CharField(
        initial='',
        label='タイトル',
        max_length=10,
        required=True,  # 必須
    )
    comment = CharField(
        initial='',
        label='コメント',
        max_length=100,
        required=True,  # 必須
    )
    def save(self):
        # save data using the self.cleaned_data dictionary
        data = self.cleaned_data
        post = Post(title=data['title'], comment=data['comment'])
        post.save()