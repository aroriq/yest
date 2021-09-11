from os import name
from django.db import models

# Create your models here.

class CustomerModel(models.Model):
    class Meta:
        verbose_name_plural = '11_顧客データ'
    lastname = models.CharField(verbose_name='姓', max_length=20, default='')
    firstname = models.CharField(verbose_name='名', max_length=20, default='')
    lastnamekana = models.CharField(verbose_name='姓（フリガナ）', max_length=20, default='')
    firstnamekana = models.CharField(verbose_name='名（フリガナ）', max_length=20, default='')
    honorific = models.CharField(verbose_name='敬称', blank=True, default='様', max_length=10)
    age = models.PositiveSmallIntegerField(verbose_name='年齢', default='', blank=True, )
    gender = models.CharField(verbose_name='性別', default='', blank=True, choices=(('1','男性'), ('2', '女性'), ('3', 'その他')), max_length=1)
    birthday = models.CharField(verbose_name='生年月日', max_length=20, blank=True, default='年月日')
    postcode = models.CharField(verbose_name='郵便番号', default='', max_length=10, blank=True, null=True)
    address1 = models.CharField(verbose_name='住所1', default='', blank=True, max_length=100)
    address2 = models.CharField(verbose_name='住所2', default='', blank=True, max_length=100)
    email = models.EmailField(verbose_name='E-mail', default='', blank=True, max_length=100, )
    tel1 = models.CharField(verbose_name='電話番号1', default='', blank=True, max_length=20,)
    tel2 = models.CharField(verbose_name='電話番号2', default='', blank=True, max_length=20,)
    fax = models.CharField(verbose_name='FAX', default='', blank=True, max_length=20, )
    moveInDate = models.DateField(verbose_name='入居日', default='', blank=True, )
    contractCategory=models.CharField(verbose_name='契約種別', default='', blank=True, max_length=10, choices=(('Rent', '賃貸'), ('Buy','購入'), ('Sell', '売却'), ('Other', 'その他')))
    contractInfo = models.CharField(verbose_name='契約情報', default='', max_length=20,)
    remarks = models.TextField(verbose_name='特記事項', blank=True, default='特記なし')
    postdate = models.DateField(verbose_name='登録日時', auto_now_add=True, null=True)
    update = models.DateField(verbose_name='更新日時', auto_now=True, null=True)

    def __str__(self):
        return "%s %s (%s)" % (self.lastname, self.firstname, self.contractInfo)
    

   
class PropertyModel(models.Model):
    class Meta:
        verbose_name_plural = '12_物件データ'
    propertyname = models.CharField(verbose_name='物件名', max_length=100, default='')
    address = models.CharField(verbose_name='住所', default='', blank=True, max_length=100)
    room = models.CharField(verbose_name='部屋番号', default='', max_length=10, blank=True, )
    madori = models.CharField(verbose_name='間取り', default='', max_length=10, blank=True, )
    floor = models.PositiveSmallIntegerField(verbose_name='階数', default='', blank=True, )
    contractCategory=models.CharField(verbose_name='契約種別', default='', blank=True, max_length=10, choices=(('Rent', '賃貸'), ('Trade','売買'), ('Other', 'その他')))
    remarks = models.TextField(verbose_name='特記事項', blank=True, default='特記なし')
    postdate = models.DateField(verbose_name='登録日時', auto_now_add=True, null=True)
    update = models.DateField(verbose_name='更新日時', auto_now=True, null=True)

    def __str__(self):
        return "%s %s" % (self.propertyname, self.room)

class CorpModel(models.Model):
    class Meta:
        verbose_name_plural = '51_店舗データ'
    
    name = models.CharField(verbose_name='店舗名', max_length=50, default='')
    postcode = models.CharField(verbose_name='郵便番号', default='', max_length=10, blank=True, null=True)
    address = models.CharField(verbose_name='住所', default='', blank=True, max_length=100)
    email = models.EmailField(verbose_name='E-mail', default='', blank=True, max_length=100, )
    tel = models.CharField(verbose_name='電話番号', default='', blank=True, max_length=20,)
    fax = models.CharField(verbose_name='FAX', default='', blank=True, max_length=20, )
    bank = models.CharField(verbose_name='銀行名', default='', blank=True, max_length=20, )
    bankbranch = models.CharField(verbose_name='支店名', default='', blank=True, max_length=20, )
    bankaccount = models.CharField(verbose_name='口座', default='', blank=True, max_length=20, )
    bankid = models.CharField(verbose_name='名義', default='', blank=True, max_length=100, )
    bankkana = models.CharField(verbose_name='フリガナ', default='', blank=True, max_length=100, )
  
    postdate = models.DateField(verbose_name='登録日時', auto_now_add=True, null=True)
    update = models.DateField(verbose_name='更新日時', auto_now=True, null=True)

    def __str__(self):
        return "%s" % (self.name)

class StaffModel(models.Model):
    class Meta:
        verbose_name_plural = '52_スタッフデータ'
    lastname = models.CharField(verbose_name='姓', max_length=20, default='')
    firstname = models.CharField(verbose_name='名', max_length=20, default='')
    lastnamekana = models.CharField(verbose_name='姓（フリガナ）', max_length=20, default='')
    firstnamekana = models.CharField(verbose_name='名（フリガナ）', max_length=20, default='')
    department=models.CharField(verbose_name='部署', default='', blank=True, max_length=10)
    age = models.PositiveSmallIntegerField(verbose_name='年齢', default='', blank=True, )
    gender = models.CharField(verbose_name='性別', default='', blank=True, choices=(('1','男性'), ('2', '女性'), ('3', 'その他')), max_length=1)
    birthday = models.CharField(verbose_name='生年月日', max_length=20, blank=True, default='年月日')
    postcode = models.CharField(verbose_name='郵便番号', default='', max_length=10, blank=True, null=True)
    address1 = models.CharField(verbose_name='住所1', default='', blank=True, max_length=100)
    address2 = models.CharField(verbose_name='住所2', default='', blank=True, max_length=100)
    email = models.EmailField(verbose_name='E-mail', default='', blank=True, max_length=100, )
    tel1 = models.CharField(verbose_name='電話番号1', default='', blank=True, max_length=20,)
    tel2 = models.CharField(verbose_name='電話番号2', default='', blank=True, max_length=20,)
    fax = models.CharField(verbose_name='FAX', default='', blank=True, max_length=20, )
    remarks = models.TextField(verbose_name='特記事項', blank=True, default='特記なし')
    postdate = models.DateField(verbose_name='登録日時', auto_now_add=True, null=True)
    update = models.DateField(verbose_name='更新日時', auto_now=True, null=True)

    def __str__(self):
        return "%s %s (%s)" % (self.lastname, self.firstname, self.department)

class ContModel(models.Model):
    class Meta:
        verbose_name_plural = '01_契約データ'
    title = models.CharField(verbose_name='契約概要', max_length=100, default='')
    customer = models.ForeignKey(CustomerModel, verbose_name='契約者', on_delete=models.PROTECT)
    property = models.ForeignKey(PropertyModel, verbose_name='物件', on_delete=models.PROTECT)
    corp = models.ForeignKey(CorpModel, verbose_name='担当店舗', on_delete=models.PROTECT, blank=True, )
    staff = models.ForeignKey(StaffModel, verbose_name='担当者', default='', on_delete=models.PROTECT, blank=True, )
    offerdate = models.DateField(verbose_name='申込日', default='', blank=True )
    contractdate = models.DateField(verbose_name='契約開始日', default='', blank=True, )
    occupdate = models.DateField(verbose_name='入居日', default='', blank=True, )
    postdate = models.DateField(verbose_name='登録日時', auto_now_add=True, null=True)
    update = models.DateField(verbose_name='更新日時', auto_now=True, null=True)
    # shikikin = models.PositiveSmallIntegerField(verbose_name='敷金', default='0', blank=True, )
    # reikin = models.PositiveSmallIntegerField(verbose_name='礼金', default='0', blank=True, )
    # yachin1 = models.PositiveSmallIntegerField(verbose_name='家賃(当月)', default='0', blank=True, )
    # yachin2 = models.PositiveSmallIntegerField(verbose_name='家賃(翌月)', default='0', blank=True, )
    # kyoekihi1 = models.PositiveSmallIntegerField(verbose_name='共益費(当月)', default='0', blank=True, )
    # kyoekihi2 = models.PositiveSmallIntegerField(verbose_name='共益費(翌月)', default='0', blank=True, )
    # chonai1 = models.PositiveSmallIntegerField(verbose_name='町内会費(当月)', default='0', blank=True, )
    # chonai2 = models.PositiveSmallIntegerField(verbose_name='町内会費(翌月)', default='0', blank=True, )
    # kanrihi1 = models.PositiveSmallIntegerField(verbose_name='管理費(当月)', default='0', blank=True, )
    # kanrihi2 = models.PositiveSmallIntegerField(verbose_name='管理費(翌月)', default='0', blank=True, )
    # park1 = models.PositiveSmallIntegerField(verbose_name='駐車場費(当月)', default='0', blank=True, )
    # park2 = models.PositiveSmallIntegerField(verbose_name='駐車場費(翌月)', default='0', blank=True, )
    # hosyo = models.PositiveSmallIntegerField(verbose_name='月額保証料', default='0', blank=True, )
    # kasai = models.PositiveSmallIntegerField(verbose_name='火災保険料', default='0', blank=True, )
    # chukai = models.PositiveSmallIntegerField(verbose_name='仲介手数料', default='0', blank=True, )
    # clean = models.PositiveSmallIntegerField(verbose_name='清掃料', default='0', blank=True, )
    # hosyoitaku = models.PositiveSmallIntegerField(verbose_name='初回保証委託料', default='0', blank=True, )
    # ff = models.PositiveSmallIntegerField(verbose_name='FF分解整備料', default='0', blank=True, )
    # cyrinder = models.PositiveSmallIntegerField(verbose_name='シリンダー交換料', default='0', blank=True, )
    # etc1 = models.PositiveSmallIntegerField(verbose_name='その他1(備考欄参照)', default='0', blank=True, )
    # etc2 = models.PositiveSmallIntegerField(verbose_name='その他2(備考欄参照)', default='0', blank=True, )
    # etc3 = models.PositiveSmallIntegerField(verbose_name='その他3(備考欄参照)', default='0', blank=True, )
    # total = models.PositiveSmallIntegerField(verbose_name='合計金額(税込)', default='0', blank=True, )
    # deposit = models.PositiveSmallIntegerField(verbose_name='合計金額(税込)', default='0', blank=True, )
    # zankin = models.PositiveSmallIntegerField(verbose_name='差引残金', default='0', blank=True, )
    # billdate = models.PositiveSmallIntegerField(verbose_name='差引残金入金日', default='0', blank=True, )
    # # 必要書類
    # jumin1 = models.BooleanField(verbose_name='入居者全員住民票(本籍省略)', default=True, blank=True, )
    # jumin2 = models.BooleanField(verbose_name='入居者全員住民票(本籍記載)', default=False, blank=True, )
    # inkan = models.BooleanField(verbose_name='印鑑証明書', default=False, blank=True, )
    # mibun = models.BooleanField(verbose_name='身分証明書写し', default=False, blank=True, )
    # hoken = models.BooleanField(verbose_name='社会保険証写し', default=False, blank=True, )
    # syotoku = models.BooleanField(verbose_name='所得証明書', default=False, blank=True, )
    # syaken = models.BooleanField(verbose_name='車検証写し', default=False, blank=True, )
    # gakusei = models.BooleanField(verbose_name='学生証写し', default=False, blank=True, )
    # zaiseki = models.BooleanField(verbose_name='在籍証明書', default=False, blank=True, )
    # naitei = models.BooleanField(verbose_name='内定通知書', default=False, blank=True, )
    # gokaku = models.BooleanField(verbose_name='合格通知書', default=False, blank=True, )
    
    # def __str__(self):
    #     return "%s (%s)" % (self.title, self.offerdate)

