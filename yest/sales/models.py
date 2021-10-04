from django.contrib.auth import get_user_model
from django.db.models import IntegerField, BooleanField, ForeignKey, DateField, DateTimeField, PositiveSmallIntegerField, Model
from django.db.models.deletion import CASCADE, PROTECT
from docs.models import ContractModel
# import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class SalesModel(Model):
    class Meta:
        verbose_name_plural = '11_売上管理'
        
    # responsiblestaff = ForeignKey(get_user_model(), verbose_name='担当者名', on_delete=CASCADE)
    responsiblestaff = ForeignKey('auth.User', verbose_name='担当者名', on_delete=PROTECT)
    contract = ForeignKey(ContractModel, verbose_name='契約データ', on_delete=PROTECT, default=None, blank=True, null=True, )
    brokerage = IntegerField(verbose_name='仲介手数料', default=0, blank=True, null=True, )
    adfee = IntegerField(verbose_name='広告料', default=0, blank=True, null=True, )
    hangingfee = IntegerField(verbose_name='事務手数料', default=0, blank=True, null=True, )
    etc1fee = IntegerField(verbose_name='その他', default=0, blank=True, null=True, )
    etc2fee = IntegerField(verbose_name='予備枠', default=0, blank=True, null=True, )
    zankin = IntegerField(verbose_name='残金', default=0, blank=True, null=True, )
    receive = BooleanField(verbose_name='回収フラグ', default=False)
    receivemonth = PositiveSmallIntegerField(verbose_name='回収月', default=None, blank=True, null=True, 
        validators=[
            MaxValueValidator(12),
            MinValueValidator(1)
        ])
    receivedate = DateField(verbose_name='回収日', default=None, blank=True, null=True, )
    created_dt = DateTimeField(verbose_name='登録日時', auto_now_add=True, blank=True, null=True)
    updated_dt = DateTimeField(verbose_name='更新日時', auto_now=True, null=True)
    corp = IntegerField(verbose_name='支店', default=None, blank=True, null=True, )

    
    def __str__(self):
        return "%s (%s)" % (self.contract, self.responsiblestaff)
    
    def price_total_include_tax(self):
        return self.brokerage + self.adfee\
             + self.hangingfee + self.etc1fee\
             + self.etc2fee

    def price_total(self):
        return round((self.brokerage + self.adfee\
             + self.hangingfee + self.etc1fee\
             + self.etc2fee)/1.1)

    # def corp(self):
    #     return self.contract.corp

# def get_corp(self):
#     return self.contract

# SalesModel.add_to_class(get_corp)
