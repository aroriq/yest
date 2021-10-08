from os import name
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime

# Create your models here.
from django.contrib.auth.models import User

def get_first_name(self):
    return "%s %s" % (self.first_name, self.last_name)

User.add_to_class("__str__", get_first_name)


class CustomerModel(models.Model):
    class Meta:
        verbose_name_plural = '11_顧客データ'
    lastname = models.CharField(verbose_name='姓', max_length=20, default='')
    firstname = models.CharField(verbose_name='名', max_length=20, default='')
    lastnamekana = models.CharField(verbose_name='姓（フリガナ）', max_length=20, default='')
    firstnamekana = models.CharField(verbose_name='名（フリガナ）', max_length=20, default='')
    completed = models.BooleanField(verbose_name='完了フラグ', default=False)
    honorific = models.CharField(verbose_name='敬称', blank=True, null=True, default='様', max_length=10)
    age = models.PositiveSmallIntegerField(verbose_name='年齢', default='', blank=True, null=True, )
    gender = models.CharField(verbose_name='性別', default='', blank=True, null=True, choices=(('1','男性'), ('2', '女性'), ('3', 'その他')), max_length=1)
    birthday = models.CharField(verbose_name='生年月日', max_length=20, blank=True, null=True, default='年月日')
    postcode = models.CharField(verbose_name='郵便番号', default='', max_length=10, blank=True, null=True)
    address1 = models.CharField(verbose_name='住所1', default='', blank=True, null=True, max_length=100)
    address2 = models.CharField(verbose_name='住所2', default='', blank=True, null=True, max_length=100)
    email = models.EmailField(verbose_name='E-mail', default='', blank=True, null=True, max_length=100, )
    tel1 = models.CharField(verbose_name='電話番号1', default='', blank=True, null=True, max_length=20,)
    tel2 = models.CharField(verbose_name='電話番号2', default='', blank=True, null=True, max_length=20,)
    fax = models.CharField(verbose_name='FAX', default='', blank=True, null=True, max_length=20, )
    moveInDate = models.DateField(verbose_name='入居日', default='', blank=True, null=True, )
    contractCategory=models.CharField(verbose_name='契約種別', default='', blank=True, null=True, max_length=10, choices=(('Rent', '賃貸'), ('Buy','購入'), ('Sell', '売却'), ('Other', 'その他')))
    contractInfo = models.CharField(verbose_name='契約情報', default='', max_length=20, blank=True, null=True, )
    remarks = models.TextField(verbose_name='特記事項', blank=True, null=True, default='特記なし')
    postdate = models.DateField(verbose_name='登録日時', auto_now_add=True, null=True)
    update = models.DateField(verbose_name='更新日時', auto_now=True, null=True)

    def __str__(self):
        return "%s %s (%s)" % (self.lastname, self.firstname, self.contractInfo)
    

   
class PropertyModel(models.Model):
    class Meta:
        verbose_name_plural = '12_物件データ'
    propertyname = models.CharField(verbose_name='物件名', max_length=100, default='')
    completed = models.BooleanField(verbose_name='完了フラグ', default=False)
    address = models.CharField(verbose_name='住所', default='', blank=True, null=True, max_length=100)
    room = models.CharField(verbose_name='部屋番号', default='', max_length=10, blank=True, null=True, )
    madori = models.CharField(verbose_name='間取り', default='', max_length=10, blank=True, null=True, )
    floor = models.PositiveSmallIntegerField(verbose_name='階数', default='', blank=True, null=True, )
    contractCategory=models.CharField(verbose_name='契約種別', default='', blank=True, null=True, max_length=10, choices=(('Rent', '賃貸'), ('Trade','売買'), ('Other', 'その他')))
    remarks = models.TextField(verbose_name='特記事項', blank=True, null=True, default='特記なし')
    postdate = models.DateField(verbose_name='登録日時', auto_now_add=True, null=True)
    update = models.DateField(verbose_name='更新日時', auto_now=True, null=True)

    def __str__(self):
        return "%s %s" % (self.propertyname, self.room)

class CorpModel(models.Model):
    class Meta:
        verbose_name_plural = '51_店舗データ'
    
    # corpname = models.CharField(verbose_name='社名', max_length=50, default='株式会社イエストホーム')
    # branch = models.CharField(verbose_name='店舗名', max_length=50, default='')
    name = models.CharField(verbose_name='店舗名', max_length=50, default='')
    postcode = models.CharField(verbose_name='郵便番号', default='', max_length=10, blank=True, null=True)
    address = models.CharField(verbose_name='住所', default='', blank=True, null=True, max_length=100)
    email = models.EmailField(verbose_name='E-mail', default='', blank=True, null=True, max_length=100, )
    tel = models.CharField(verbose_name='電話番号', default='', blank=True, null=True, max_length=20,)
    fax = models.CharField(verbose_name='FAX', default='', blank=True, null=True, max_length=20, )
    bank = models.CharField(verbose_name='銀行名', default='', blank=True, null=True, max_length=20, )
    bankbranch = models.CharField(verbose_name='支店名', default='', blank=True, null=True, max_length=20, )
    bankaccount = models.CharField(verbose_name='口座', default='', blank=True, null=True, max_length=20, )
    bankid = models.CharField(verbose_name='名義', default='', blank=True, null=True, max_length=100, )
    bankkana = models.CharField(verbose_name='フリガナ', default='', blank=True, null=True, max_length=100, )
  
    postdate = models.DateField(verbose_name='登録日時', auto_now_add=True, null=True)
    update = models.DateField(verbose_name='更新日時', auto_now=True, null=True)

    def __str__(self):
        return "%s" % (self.name)

class KanriModel(models.Model):
    class Meta:
        verbose_name_plural = '31_管理会社データ'
    
    name = models.CharField(verbose_name='管理会社名', max_length=50, default='')
    postcode = models.CharField(verbose_name='郵便番号', default='', max_length=10, blank=True, null=True)
    address = models.CharField(verbose_name='住所', default='', blank=True, null=True, max_length=100)
    email = models.EmailField(verbose_name='E-mail', default='', blank=True, null=True, max_length=100, )
    tel = models.CharField(verbose_name='電話番号', default='', blank=True, null=True, max_length=20,)
    fax = models.CharField(verbose_name='FAX', default='', blank=True, null=True, max_length=20, )
    postdate = models.DateField(verbose_name='登録日時', auto_now_add=True, null=True)
    update = models.DateField(verbose_name='更新日時', auto_now=True, null=True)

    def __str__(self):
        return "%s" % (self.name)

class TransModel(models.Model):
    class Meta:
        verbose_name_plural = '32_引越会社データ'
    name = models.CharField(verbose_name='引越会社名', max_length=50, default='')
    postcode = models.CharField(verbose_name='郵便番号', default='', max_length=10, blank=True, null=True)
    address = models.CharField(verbose_name='住所', default='', blank=True, null=True, max_length=100)
    email = models.EmailField(verbose_name='E-mail', default='', blank=True, null=True, max_length=100, )
    tel = models.CharField(verbose_name='電話番号', default='', blank=True, null=True, max_length=20,)
    fax = models.CharField(verbose_name='FAX', default='', blank=True, null=True, max_length=20, )
    postdate = models.DateField(verbose_name='登録日時', auto_now_add=True, null=True)
    update = models.DateField(verbose_name='更新日時', auto_now=True, null=True)

    def __str__(self):
        return "%s" % (self.name)

class GuarantModel(models.Model):
    class Meta:
        verbose_name_plural = '33_保証会社データ'
    name = models.CharField(verbose_name='保証会社名', max_length=50, default='')
    postcode = models.CharField(verbose_name='郵便番号', default='', max_length=10, blank=True, null=True)
    address = models.CharField(verbose_name='住所', default='', blank=True, null=True, max_length=100)
    email = models.EmailField(verbose_name='E-mail', default='', blank=True, null=True, max_length=100, )
    tel = models.CharField(verbose_name='電話番号', default='', blank=True, null=True, max_length=20,)
    fax = models.CharField(verbose_name='FAX', default='', blank=True, null=True, max_length=20, )
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
    # nameen = models.CharField(verbose_name='Lastname Firstname', max_length=100, default='')
    department=models.CharField(verbose_name='部署', default='', blank=True, null=True, max_length=10)
    age = models.PositiveSmallIntegerField(verbose_name='年齢', default='', blank=True, null=True, )
    gender = models.CharField(verbose_name='性別', default='', blank=True, null=True, choices=(('1','男性'), ('2', '女性'), ('3', 'その他')), max_length=1)
    birthday = models.DateField(verbose_name='生年月日', blank=True, null=True, default='2000-01-01')
    postcode = models.CharField(verbose_name='郵便番号', default='', max_length=10, blank=True, null=True)
    address1 = models.CharField(verbose_name='住所1', default='', blank=True, null=True, max_length=100)
    address2 = models.CharField(verbose_name='住所2', default='', blank=True, null=True, max_length=100)
    email = models.EmailField(verbose_name='E-mail', default='', blank=True, null=True, max_length=100, )
    tel1 = models.CharField(verbose_name='電話番号1', default='', blank=True, null=True, max_length=20,)
    tel2 = models.CharField(verbose_name='電話番号2', default='', blank=True, null=True, max_length=20,)
    fax = models.CharField(verbose_name='FAX', default='', blank=True, null=True, max_length=20, )
    remarks = models.TextField(verbose_name='特記事項', blank=True, null=True, default='特記なし')
    postdate = models.DateField(verbose_name='登録日時', auto_now_add=True, null=True)
    update = models.DateField(verbose_name='更新日時', auto_now=True, null=True)

    def __str__(self):
        return "%s %s (%s)" % (self.lastname, self.firstname, self.department)

class ContractModel(models.Model):
    class Meta:
        verbose_name_plural = '01_契約データ'
    title = models.CharField(verbose_name='契約ID', max_length=100, default='')
    completed = models.BooleanField(verbose_name='完了フラグ', default=False)
    customer = models.ForeignKey(CustomerModel, verbose_name='契約者', on_delete=models.PROTECT)
    property = models.ForeignKey(PropertyModel, verbose_name='物件', on_delete=models.PROTECT)
    corp = models.ForeignKey(CorpModel, verbose_name='担当店舗', on_delete=models.PROTECT, blank=True, null=True, )
    responsiblestaff = models.ForeignKey('auth.User', verbose_name='責任担当者', default='', on_delete=models.PROTECT, blank=True, null=True, )
    # staff = models.ForeignKey(StaffModel, verbose_name='担当者', default='', on_delete=models.PROTECT, blank=True, null=True, )
    guarant = models.ForeignKey(GuarantModel, verbose_name='保証会社', on_delete=models.PROTECT)
    gas = models.CharField(verbose_name='ガス会社', default='', max_length=50, blank=True, null=True, )
    offerdate = models.DateField(verbose_name='申込日', default=None, blank=True )
    contractdate = models.DateField(verbose_name='契約開始日', auto_now=True,  null=True, )
    occupdate = models.DateField(verbose_name='入居日', default=None, blank=True, null=True, )
    postdate = models.DateField(verbose_name='登録日時', auto_now_add=True, blank=True, null=True)
    update = models.DateField(verbose_name='更新日時', auto_now=True, null=True)
    month1 = models.IntegerField(verbose_name='当月', default=datetime.datetime.today().month, blank=True, null=True, 
                                              validators=[MinValueValidator(1),
                                                          MaxValueValidator(12)]
                                                          )
    month2 = models.PositiveSmallIntegerField(verbose_name='翌月', default=datetime.datetime.today().month+1, blank=True, null=True, )
    shikikin = models.PositiveSmallIntegerField(verbose_name='敷金', default=0, blank=True, null=True, )
    reikin = models.PositiveSmallIntegerField(verbose_name='礼金', default=0, blank=True, null=True, )
    yachin1 = models.PositiveSmallIntegerField(verbose_name='家賃(当月)', default=0, blank=True, null=True, )
    yachin2 = models.PositiveSmallIntegerField(verbose_name='家賃(翌月)', default=0, blank=True, null=True, )
    kyoekihi1 = models.PositiveSmallIntegerField(verbose_name='共益費(当月)', default=0, blank=True, null=True, )
    kyoekihi2 = models.PositiveSmallIntegerField(verbose_name='共益費(翌月)', default=0, blank=True, null=True, )
    chonai1 = models.PositiveSmallIntegerField(verbose_name='町内会費(当月)', default=0, blank=True, null=True, )
    chonai2 = models.PositiveSmallIntegerField(verbose_name='町内会費(翌月)', default=0, blank=True, null=True, )
    kanrihi1 = models.PositiveSmallIntegerField(verbose_name='管理費(当月)', default=0, blank=True, null=True, )
    kanrihi2 = models.PositiveSmallIntegerField(verbose_name='管理費(翌月)', default=0, blank=True, null=True, )
    park1 = models.PositiveSmallIntegerField(verbose_name='駐車場費(当月)', default=0, blank=True, null=True, )
    park2 = models.PositiveSmallIntegerField(verbose_name='駐車場費(翌月)', default=0, blank=True, null=True, )
    item1 = models.CharField(verbose_name='項目1', default='月額保証料', max_length=50, blank=True, null=True, )
    hosyo = models.SmallIntegerField(verbose_name='項目1金額', default=0, blank=True, null=True, )
    item2 = models.CharField(verbose_name='項目2', default='火災保険料', max_length=50, blank=True, null=True, )
    kasai = models.SmallIntegerField(verbose_name='項目2金額', default=0, blank=True, null=True, )
    item3 = models.CharField(verbose_name='項目3', default='仲介手数料', max_length=50, blank=True, null=True, )
    brokerage = models.SmallIntegerField(verbose_name='項目3金額', default=0, blank=True, null=True, )
    item4 = models.CharField(verbose_name='項目4', default='清掃料', max_length=50, blank=True, null=True, )
    etc3 = models.SmallIntegerField(verbose_name='項目4金額', default=0, blank=True, null=True, )
    item5 = models.CharField(verbose_name='項目5', default='初回保証委託料', max_length=50, blank=True, null=True, )
    hosyoitaku = models.SmallIntegerField(verbose_name='項目5金額', default=0, blank=True, null=True, )
    item6 = models.CharField(verbose_name='項目6', default='FF分解整備料', max_length=50, blank=True, null=True, )
    ff = models.SmallIntegerField(verbose_name='項目6金額', default=0, blank=True, null=True, )
    item7 = models.CharField(verbose_name='項目7', default='シリンダー交換料', max_length=50, blank=True, null=True, )
    cyrinder = models.SmallIntegerField(verbose_name='項目7金額', default=0, blank=True, null=True, )
    item8 = models.CharField(verbose_name='項目8', default='', max_length=50, blank=True, null=True, )
    item8bill = models.SmallIntegerField(verbose_name='項目8金額', default=0, blank=True, null=True, )
    item9 = models.CharField(verbose_name='項目9', default='', max_length=50, blank=True, null=True, )
    itemb9ill = models.SmallIntegerField(verbose_name='項目9金額', default=0, blank=True, null=True, )
    total = models.PositiveSmallIntegerField(verbose_name='合計金額(税込)', default=None, blank=True, null=True, )
    deposit = models.PositiveSmallIntegerField(verbose_name='手付金', default=0, blank=True, null=True, )
    zankin = models.PositiveSmallIntegerField(verbose_name='差引残金', default=None, blank=True, null=True, )
    limit = models.DateField(verbose_name='差引残金期日', default=None, blank=True, null=True)
    etcitem1 = models.CharField(verbose_name='上記外項目1', default='火災保険料(2年)', max_length=50, blank=True, null=True, )
    etcitem1bill = models.SmallIntegerField(verbose_name='上記外項目1金額', default=0, blank=True, null=True, )
    etcitem2 = models.CharField(verbose_name='上記外項目2', default='ハウスクリーニング料(退去時)', max_length=50, blank=True, null=True, )
    etcitem2bill = models.SmallIntegerField(verbose_name='上記外項目2金額', default=0, blank=True, null=True, )
    etcitem3 = models.CharField(verbose_name='上記外項目3', default='シリンダー交換料(退去時)', max_length=50, blank=True, null=True, )
    etcitem3bill = models.SmallIntegerField(verbose_name='上記外項目3金額', default=0, blank=True, null=True, )
    adfee = models.SmallIntegerField(verbose_name='広告料金額', default=0, blank=True, null=True, )
    doc1 = models.CharField(verbose_name='必要書類1', default='入居者全員住民票(本籍省略)', max_length=50, blank=True, null=True, )
    doc1a = models.BooleanField(verbose_name='必要書類1_契約者', default=False, blank=True, null=True, )
    doc1b = models.BooleanField(verbose_name='必要書類1_同居人', default=False, blank=True, null=True, )
    doc1c = models.BooleanField(verbose_name='必要書類1_連帯保証人', default=False, blank=True, null=True, )
    doc2 = models.CharField(verbose_name='必要書類2', default='入居者全員住民票(本籍記載)', max_length=50, blank=True, null=True, )
    doc2a = models.BooleanField(verbose_name='必要書類2_契約者', default=False, blank=True, null=True, )
    doc2b = models.BooleanField(verbose_name='必要書類2_同居人', default=False, blank=True, null=True, )
    doc2c = models.BooleanField(verbose_name='必要書類2_連帯保証人', default=False, blank=True, null=True, )
    doc3 = models.CharField(verbose_name='必要書類3', default='印鑑証明書', max_length=50, blank=True, null=True, )
    doc3a = models.BooleanField(verbose_name='必要書類3_契約者', default=False, blank=True, null=True, )
    doc3b = models.BooleanField(verbose_name='必要書類3_同居人', default=False, blank=True, null=True, )
    doc3c = models.BooleanField(verbose_name='必要書類3_連帯保証人', default=False, blank=True, null=True, )
    doc4 = models.CharField(verbose_name='必要書類4', default='身分証明書写し', max_length=50, blank=True, null=True, )
    doc4a = models.BooleanField(verbose_name='必要書類4_契約者', default=False, blank=True, null=True, )
    doc4b = models.BooleanField(verbose_name='必要書類4_同居人', default=False, blank=True, null=True, )
    doc4c = models.BooleanField(verbose_name='必要書類4_連帯保証人', default=False, blank=True, null=True, )
    doc5 = models.CharField(verbose_name='必要書類5', default='社会保険証写し', max_length=50, blank=True, null=True, )
    doc5a = models.BooleanField(verbose_name='必要書類5_契約者', default=False, blank=True, null=True, )
    doc5b = models.BooleanField(verbose_name='必要書類5_同居人', default=False, blank=True, null=True, )
    doc5c = models.BooleanField(verbose_name='必要書類5_連帯保証人', default=False, blank=True, null=True, )
    doc6 = models.CharField(verbose_name='必要書類6', default='所得証明書', max_length=50, blank=True, null=True, )
    doc6a = models.BooleanField(verbose_name='必要書類6_契約者', default=False, blank=True, null=True, )
    doc6b = models.BooleanField(verbose_name='必要書類6_同居人', default=False, blank=True, null=True, )
    doc6c = models.BooleanField(verbose_name='必要書類6_連帯保証人', default=False, blank=True, null=True, )
    doc7 = models.CharField(verbose_name='必要書類7', default='車検証写し', max_length=50, blank=True, null=True, )
    doc7a = models.BooleanField(verbose_name='必要書類7_契約者', default=False, blank=True, null=True, )
    doc7b = models.BooleanField(verbose_name='必要書類7_同居人', default=False, blank=True, null=True, )
    doc7c = models.BooleanField(verbose_name='必要書類7_連帯保証人', default=False, blank=True, null=True, )
    doc8 = models.CharField(verbose_name='必要書類8', default='学生証写し', max_length=50, blank=True, null=True, )
    doc8a = models.BooleanField(verbose_name='必要書類8_契約者', default=False, blank=True, null=True, )
    doc8b = models.BooleanField(verbose_name='必要書類8_同居人', default=False, blank=True, null=True, )
    doc8c = models.BooleanField(verbose_name='必要書類8_連帯保証人', default=False, blank=True, null=True, )
    doc9 = models.CharField(verbose_name='必要書類9', default='在籍証明書', max_length=50, blank=True, null=True, )
    doc9a = models.BooleanField(verbose_name='必要書類9_契約者', default=False, blank=True, null=True, )
    doc9b = models.BooleanField(verbose_name='必要書類9_同居人', default=False, blank=True, null=True, )
    doc9c = models.BooleanField(verbose_name='必要書類9_連帯保証人', default=False, blank=True, null=True, )
    doca = models.CharField(verbose_name='必要書類10', default='内定通知書', max_length=50, blank=True, null=True, )
    docaa = models.BooleanField(verbose_name='必要書類10_契約者', default=False, blank=True, null=True, )
    docab = models.BooleanField(verbose_name='必要書類10_同居人', default=False, blank=True, null=True, )
    docac = models.BooleanField(verbose_name='必要書類10_連帯保証人', default=False, blank=True, null=True, )
    docb = models.CharField(verbose_name='必要書類11', default='合格通知書', max_length=50, blank=True, null=True, )
    docba = models.BooleanField(verbose_name='必要書類11_契約者', default=False, blank=True, null=True, )
    docbb = models.BooleanField(verbose_name='必要書類11_同居人', default=False, blank=True, null=True, )
    docbc = models.BooleanField(verbose_name='必要書類11_連帯保証人', default=False, blank=True, null=True, )
    remarks = models.TextField(verbose_name='特記事項', blank=True, null=True, default='')
    jsdate = models.DateField(verbose_name='重説実施日', default=None, blank=True, null=True,  )
    submitdoc = models.TextField(verbose_name='契約費明細　提出書類', blank=True, null=True, \
        default='・建物賃貸借契約書（2部）\n・使用規則（2部）\n・原状回復の条件について（2部）\n・鍵預り証（1部）\n・リペアサービス申込書（1部）\n・保証会社申込書類（1式）\n・重要事項説明書写し（仲介業者書式）\n\n・火災保険加入書類\n・御入居者様へのご案内\n・物件状況チェックリスト')
    zanmuremarks = models.TextField(verbose_name='残務処理特記事項', blank=True, null=True, default='')
    reportdoc = models.TextField(verbose_name='契約関係書類報告書　添付書類', blank=True, null=True, \
        default='・入居申込書\n・契約書コピー（別紙特約、覚書等）\n・重説控え（原本）\n・保証会社申込書（身分証明書等含）\n・保証会社承認通知書\n・保証会社契約書控え（コピー）\n・鍵受領書\n・')
    reportremarks = models.TextField(verbose_name='契約関係書類報告書　備考', blank=True, null=True, default='')
    key1name = models.CharField(verbose_name='鍵A(番号)', default='部屋', max_length=50, blank=True, null=True, )
    key1 = models.PositiveSmallIntegerField(verbose_name='鍵A本数', default=1, blank=True, null=True, )
    key2name = models.CharField(verbose_name='鍵B(番号)', default='車庫', max_length=50, blank=True, null=True, )
    key2 = models.PositiveSmallIntegerField(verbose_name='鍵B本数', default=0, blank=True, null=True, )
    key3name = models.CharField(verbose_name='鍵C(番号)', default='トランクルーム', max_length=50, blank=True, null=True, )
    key3 = models.PositiveSmallIntegerField(verbose_name='鍵C本数', default=0, blank=True, null=True, )
    kanri = models.ForeignKey(KanriModel, verbose_name='管理会社', on_delete=models.PROTECT)
    kanristaff = models.CharField(verbose_name='管理会社担当者名', default='ご担当者様', max_length=50, blank=True, null=True, )
    kanridoc = models.TextField(verbose_name='管理会社宛FAX　本文', blank=True, null=True,  
        default='拝啓　時下益々ご清栄のこととお慶び申し上げます。\n\n', )
    trans = models.ForeignKey(TransModel, verbose_name='引越業者', on_delete=models.PROTECT)
    transstaff = models.CharField(verbose_name='引越業者担当者名', default='ご担当者様', max_length=50, blank=True, null=True, )
    transdate = models.TextField(verbose_name='引越連絡希望日', default='第1希望 月　日　:  ～　: \n\n第2希望 月　日　:  ～　: \n\n第3希望 月　日　:  ～　: ', blank=True, null=True,  )
    transremarks = models.TextField(verbose_name='引越見積依頼書　備考', default='拝啓　時下ますますご清栄のこととお慶び申し上げます。', blank=True, null=True,  )
    receipt_date = models.DateField(verbose_name='領収書　発行日', default=None, blank=True, null=True,  )
    receipt_atena = models.CharField(verbose_name='領収書　宛名', default='', max_length=50, blank=True, null=True, )  
    receipt_meimo = models.CharField(verbose_name='領収書　但し書き', default='', max_length=50, blank=True, null=True, )  
    receipt_total = models.PositiveSmallIntegerField(verbose_name='領収書　合計金額', default=0, blank=True, null=True, )
    receiptremarks1 = models.TextField(verbose_name='領収書　備考', default='', blank=True, null=True,  )
    azukari_date = models.DateField(verbose_name='預り書　発行日', default=None, blank=True, null=True,  )
    azukari_atena = models.CharField(verbose_name='預り証　宛名', default='', max_length=50, blank=True, null=True, )  
    azukari_meimo = models.CharField(verbose_name='預り証　但し書き', default='', max_length=50, blank=True, null=True, )  
    azukari_total = models.PositiveSmallIntegerField(verbose_name='預り証　合計金額', default=0, blank=True, null=True, )
    azukari_remarks2 = models.TextField(verbose_name='預り証　備考', default='', blank=True, null=True,  )
    # sum = models.PositiveSmallIntegerField(verbose_name='合計金額(税込)', editable=False, blank=True, null=True, default=None)
    def __str__(self):
        return "%s (%s) (%s)" % (self.title, self.offerdate, self.responsiblestaff.first_name)
    
    def price_total(self):
        return self.shikikin + self.reikin\
             + self.yachin1 + self.yachin2\
             + self.kyoekihi1 + self.kyoekihi2\
             + self.chonai1 + self.chonai2\
             + self.kanrihi1 + self.kanrihi2\
             + self.park1 + self.park2\
             + self.hosyo\
             + self.kasai\
             + self.brokerage\
             + self.etc3\
             + self.hosyoitaku\
             + self.ff\
             + self.cyrinder\
             + self.item8bill\
             + self.itemb9ill

    def remain_bill(self):
        return self.price_total() - self.deposit



class Post(models.Model):
    """投稿モデル"""
    class Meta:
        db_table = 'post'
    title = models.CharField(verbose_name='タイトル', max_length=10)
    comment = models.CharField(verbose_name='コメント', max_length=100)
    created_at = models.DateTimeField(verbose_name='登録日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)
    def __str__(self):
        return self.title + ',' + self.comment