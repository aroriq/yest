from os import name
from django.db import models

# Create your models here.
#CustomerCategory=(('Rent', '賃貸'), ('Buy','購入'), ('Sell', '売却'))

class CustomerModel(models.Model):
    class Meta:
        verbose_name_plural = '顧客管理データ'
    lastname = models.CharField(verbose_name='姓', max_length=20, default='')
    firstname = models.CharField(verbose_name='名', max_length=20, default='')
    honorific = models.CharField(verbose_name='敬称', blank=True, null=True, default='様', max_length=10)
    age = models.PositiveSmallIntegerField(verbose_name='年齢', blank=True, null=True, )
    gender = models.CharField(verbose_name='性別', blank=True, null=True, choices=(('1','男性'), ('2', '女性'), ('3', 'その他')), max_length=1)
    birthday = models.CharField(verbose_name='生年月日', max_length=20, blank=True, null=True, default='年月日')
    postcode = models.CharField(verbose_name='郵便番号', max_length=10, blank=True, null=True)
    address1 = models.CharField(verbose_name='住所1', blank=True, null=True, max_length=100)
    address2 = models.CharField(verbose_name='住所2', blank=True, null=True, max_length=100)
    email = models.EmailField(verbose_name='E-mail', blank=True, null=True, max_length=100, )
    tel1 = models.CharField(verbose_name='電話番号1', blank=True, null=True, max_length=20,)
    tel2 = models.CharField(verbose_name='電話番号2', blank=True, null=True, max_length=20,)
    fax = models.CharField(verbose_name='FAX', blank=True, null=True, max_length=20, )
    moveInDate = models.DateField(verbose_name='入居日', blank=True, null=True, )
    contractCategory=models.CharField(verbose_name='契約種別', blank=True, null=True, max_length=10, choices=(('Rent', '賃貸'), ('Buy','購入'), ('Sell', '売却'), ('Other', 'その他')))
    contractInfo = models.CharField(verbose_name='契約情報', max_length=20, default='物件名等')
    remarks = models.TextField(verbose_name='特記事項', blank=True, null=True, default='特記なし')
    postdate = models.DateField(verbose_name='登録日時', auto_now_add=True, null=True)
    update = models.DateField(verbose_name='更新日時', auto_now=True, null=True)

    def __str__(self):
        return "%s %s (%s)" % (self.lastname, self.firstname, self.contractInfo)
    

