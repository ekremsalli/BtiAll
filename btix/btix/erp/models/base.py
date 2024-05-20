"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.db import models
from django.db.models.lookups import In

class BaseVAT(models.Model):
    vat = models.FloatField(
        db_column='VAT',
        blank=True,
        null=True,
        help_text='KDV'
    )
    class Meta:
        abstract = True

class BaseCharset(models.Model):
    charsetref = models.IntegerField(
        db_column='CHARSETREF', blank=True, null=True)
    class Meta:
        abstract = True

class BaseWFlowTask(models.Model):
    wflowcrdref = models.ForeignKey(
        "LG_WFTASK",
        db_column='WFLOWCRDREF',
        help_text='İş akış kartı ref.',
        blank=True,
        null=True,
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_wflowcrdref"
    )
    class Meta:
        abstract = True


class BaseAddTax(models.Model):
    addtaxref = models.ForeignKey(
        "LG_ADDTAX",
        db_column='ADDTAXREF',
        blank=True,
        null=True,
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_addtaxref"
    )
    class Meta:
        abstract = True

class BasePrint(models.Model):
    printcnt = models.SmallIntegerField(
        db_column='PRINTCNT',
        blank=True,
        null=True,
        help_text='Basılmış toplam hesap'
    )
    class Meta:
        abstract = True

class BaseSign(models.Model):
    sign = models.SmallIntegerField(
        db_column='SIGN',
        blank=True,
        null=True,
        help_text='Borç/Alacak işareti'
    )
    class Meta:
        abstract = True

class BaseAccounted(models.Model):
    accounted = models.SmallIntegerField(
        db_column='ACCOUNTED',
        blank=True,
        null=True,
        help_text='Muhasebeleştirildi'
    )
    class Meta:
        abstract = True

class BaseCancelled(models.Model):
    cancelled = models.SmallIntegerField(
        db_column='CANCELLED',
        blank=True,
        null=True,
        help_text='İptal edilmiş'
    )
    class Meta:
        abstract = True

class BaseMontly(models.Model):
    debit = models.FloatField(
        db_column='DEBIT',
        blank=True,
        null=True,
        help_text='Borç'
    )
    credit = models.FloatField(
        db_column='CREDIT',
        blank=True,
        null=True,
        help_text='Alacak'
    )

    class Meta:
        abstract = True

class BaseApproved(models.Model):
    approved = models.SmallIntegerField(
        db_column='APPROVED',
        blank=True,
        null=True,
        choices=[
            (0, 'Onaylı'),
            (1, 'Onaysız')
        ],
        help_text='Onay bilgisi'
    )
    class Meta:
        abstract = True

class BaseClient(models.Model):
    clientref = models.ForeignKey(
        "LG_CLCARD",
        db_column='CLIENTREF',
        blank=True,
        null=True,
        help_text='Cari hesap ref. -> CLCARD',
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_clientref"
    )
    class Meta:
        abstract = True


class BaseItem(models.Model):
    itemref = models.ForeignKey(
        "LG_ITEMS",
        db_column='ITEMREF',
        blank=True,
        null=True,
        help_text='Malzeme kartı ref. -> ITEM',
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_itemref"
    )
    class Meta:
        abstract = True


class BaseAmount(models.Model):
    amount = models.FloatField(
        db_column='AMOUNT',
        blank=True,
        null=True,
        help_text='Miktar'
    )
    class Meta:
        abstract = True

class BaseUnitSet(models.Model):
    uomref = models.ForeignKey(
        "LG_UNITSETL",
        db_column='UOMREF',
        blank=True,
        null=True,
        help_text='Birim ref. -> UNITSETL',
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_uomref"
    )
    class Meta:
        abstract = True

class BaseUnit(models.Model):
    uomref = models.ForeignKey(
        "LG_UNITSETL",
        db_column='UOMREF',
        blank=True,
        null=True,
        help_text='Birim ref. -> UNITSETL',
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_uomref"
    )
    usref = models.ForeignKey(
        "LG_UNITSETF",
        db_column='USREF',
        blank=True,
        null=True,
        help_text='Birim seti ref. -> UNITSETF',
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_usref"
    )
    uinfo1 = models.FloatField(
        db_column='UINFO1',
        blank=True,
        null=True,
        help_text='Çevrim katsayısı'
    )
    uinfo2 = models.FloatField(
        db_column='UINFO2',
        blank=True,
        null=True,
        help_text='Çevrim katsayısı'
    )
    uinfo3 = models.FloatField(
        db_column='UINFO3',
        blank=True,
        null=True,
        help_text='Boyut katsayısı'
    )
    uinfo4 = models.FloatField(
        db_column='UINFO4',
        blank=True,
        null=True,
        help_text='Boyut katsayısı'
    )
    uinfo5 = models.FloatField(
        db_column='UINFO5',
        blank=True,
        null=True,
        help_text='Boyut katsayısı'
    )
    uinfo6 = models.FloatField(
        db_column='UINFO6',
        blank=True,
        null=True,
        help_text='Boyut katsayısı'
    )
    uinfo7 = models.FloatField(
        db_column='UINFO7',
        blank=True,
        null=True,
        help_text='Boyut katsayısı'
    )
    uinfo8 = models.FloatField(
        db_column='UINFO8',
        blank=True,
        null=True,
        help_text='Boyut katsayısı'
    )

    class Meta:
        abstract = True

class BaseSalesMan(models.Model):
    salesmanref = models.ForeignKey(
        "LG_SLSMAN",
        db_column='SALESMANREF',
        blank=True,
        null=True,
        help_text='Satış elemanı ref -> SLSMAN',
        on_delete=models.DO_NOTHING
    )
    class Meta:
        abstract = True

class BaseBranch(models.Model):
    branch = models.SmallIntegerField(
        db_column='BRANCH',
        blank=True,
        null=True,
        help_text='İşyeri'
    )
    class Meta:
        abstract = True

class BaseBranchNr(models.Model):
    branchnr = models.SmallIntegerField(
        db_column='BRANCHNR',
        blank=True,
        null=True
    )
    class Meta:
        abstract = True


class BaseDepartment(models.Model):
    deparment = models.SmallIntegerField(
        db_column='DEPARMENT',
        blank=True,
        null=True,
        help_text='Bölüm'
    )
    class Meta:
        abstract = True

class BaseProject(models.Model):
    projectref = models.ForeignKey(
        "LG_PROJECT",
        db_column='PROJECTREF',
        blank=True,
        null=True,
        help_text='Proje ref.',
        on_delete=models.DO_NOTHING
    )
    class Meta:
        abstract = True

class BaseModule(models.Model):
    modnr = models.SmallIntegerField(
        db_column='MODNR',
        blank=True,
        null=True,
        help_text='Modül numarası')
    class Meta:
        abstract = True

class BaseGUID(models.Model):
    guid = models.CharField(
        db_column='GUID',
        max_length=37,
        blank=True,
        null=True
    )
    class Meta:
        abstract = True

class BaseRef(models.Model):
    orglogicref = models.ForeignKey(
        'self',
        db_column='ORGLOGICREF',
        blank=True,
        null=True,
        help_text='Orjinal kayıt ref.',
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_orglogicref"
    )
    class Meta:
        abstract = True

class BaseCard(models.Model):
    cardref = models.ForeignKey(
        'LG_ITEMS',
        db_column='CARDREF',
        blank=True,
        null=True,
        help_text='Kart referansı -> ITEMS',
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_item"
    )
    class Meta:
        abstract = True

class BaseLogical(models.Model):
    logicalref = models.AutoField(
        db_column='LOGICALREF',
        primary_key=True,
        help_text='Fiziksel adres'
    )
    class Meta:
        abstract = True

    @classmethod
    def next_code(cls, field, sablon, numaralama, merge='.', exclude=None, filter=None):
        # field -> code
        # numaralama -> 120.01
        # sablon -> 00000
        from django.db.models import BigIntegerField
        from django.db.models.functions import Length
        from django.db.models.functions import Cast
        from django.db.models.functions import Substr
        let = len(sablon)
        if len(merge):
            let += 1
        let += len(numaralama)
        fx = {
            'text_len': let,
            f'{field}__startswith': numaralama
        }
        begin = cls.objects
        if exclude:
            begin = begin.exclude(**exclude)
        if filter:
            begin = begin.filter(**filter)

        if len(merge):
            next_code = begin.annotate(
                text_len=Length(field)).filter(**fx).aggregate(
                    next=models.Max(field))
        else:
            next_code = begin.annotate(
                text_len=Length(field)).filter(**fx).annotate(
                    val=Cast(Substr(field, len(sablon)), output_field=BigIntegerField())).aggregate(
                    next=models.Max('val'))

        if next_code['next'] is None:
            code = "1".zfill(len(sablon))
            code = f"{numaralama}{merge}{code}"
        else:
            if len(merge):
                code = next_code['next']
                _, ncode = code.split(numaralama)
                code = int(ncode[1:]) + 1
                code = str(code).zfill(len(sablon))
                code = f"{numaralama}{merge}{code}"
            else:
                code = next_code['next']
                code = str(int(code) + 1)
                code = f"{numaralama}{merge}{code[-len(sablon):]}"

                
        return code


class BasePriority(models.Model):
    priority = models.SmallIntegerField(
        db_column='PRIORITY',
        blank=True,
        null=True
    )
    class Meta:
        abstract = True


class BaseAccount(models.Model):
    accountref = models.ForeignKey(
        'LG_EMUHACC',
        db_column='ACCOUNTREF',
        blank=True,
        null=True,
        help_text='Genel muhasebe hesabı ref. -> EMUHACC',
        to_field='logicalref',
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_accountref"
    )
    class Meta:
        abstract = True

class BaseCenter(models.Model):
    centerref = models.ForeignKey(
        'LG_EMCENTER',
        db_column='CENTERREF',
        blank=True,
        null=True,
        help_text='Masraf merkezi ref. -> EMCENTER',
        to_field='logicalref',
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_centerref"
    )
    class Meta:
        abstract = True

class BaseActive(models.Model):
    active = models.SmallIntegerField(
        db_column='ACTIVE',
        blank=True,
        null=True,
        choices=[
            (0, 'Kullanımda'),
            (1, 'Kullanım dışı')
        ],
        help_text='Durum'
    )
    class Meta:
        abstract = True


class BasePayment(models.Model):
    paymentref = models.ForeignKey(
        'LG_PAYPLANS',
        db_column='PAYMENTREF',
        blank=True,
        null=True,
        help_text='Ödeme planı ref. -> PAYPLANS',
        to_field='logicalref',
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_payref"
    )
    class Meta:
        abstract = True

class BaseBank(models.Model):
    bankref = models.ForeignKey(
        'LG_BNCARD',
        db_column='BANKREF',
        blank=True,
        null=True,
        help_text='Banka ref. -> BNCARD',
        to_field='logicalref',
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_bankref"
    )
    class Meta:
        abstract = True

class BaseSiteRec(models.Model):
    siteid = models.SmallIntegerField(
        db_column='SITEID',
        blank=True,
        null=True,
        help_text='Bölge no'
    )
    recstatus = models.SmallIntegerField(
        db_column='RECSTATUS',
        blank=True,
        null=True,
        help_text='Kayıt durumu'
    )
    class Meta:
        abstract = True

class BaseCode(models.Model):
    specode = models.CharField(
        db_column='SPECODE',
        max_length=11,
        blank=True,
        null=True,
        help_text='Özel kod (AUXIL_CODE)'
    )
    cyphcode = models.CharField(
        db_column='CYPHCODE',
        max_length=11,
        blank=True,
        null=True,
        help_text='Yetki kodu (AUTH_CODE)'
    )
    class Meta:
        abstract = True

class BaseContact(models.Model):
    telnrs1 = models.CharField(db_column='TELNRS1', max_length=16,
        blank=True, null=True, help_text='Telefon numarası (1)')
    telnrs2 = models.CharField(db_column='TELNRS2', max_length=16, blank=True,
        null=True, help_text='Telefon numarası (2)')
    faxnr = models.CharField(db_column='FAXNR', max_length=16, blank=True,
        null=True, help_text='Faks numarası')
    emailaddr = models.CharField(db_column='EMAILADDR', max_length=51,
        blank=True, null=True, help_text='E-posta adresi')

    """
    telcodes1 = models.CharField(db_column='TELCODES1', max_length=9,
        blank=True, null=True)
    telcodes2 = models.CharField(db_column='TELCODES2',
        max_length=9, blank=True, null=True)
    faxcode = models.CharField(db_column='FAXCODE',
        max_length=9, blank=True, null=True)
    """
    class Meta:
        abstract = True

class BaseTrading(models.Model):
    tradinggrp = models.CharField(
        db_column='TRADINGGRP',
        max_length=17,
        blank=True,
        null=True,
        help_text='Ticari işlem grubu'
    )
    class Meta:
        abstract = True

class BaseTax(models.Model):
    vatnr = models.CharField(db_column='VATNR', max_length=33,
        blank=True, null=True, help_text='KDV numarası')
    taxnr = models.CharField(db_column='TAXNR', max_length=16, blank=True,
        null=True, help_text='Vergi numarası')
    taxoffice = models.CharField(db_column='TAXOFFICE', max_length=16,
        blank=True, null=True, help_text='Vergi dairesi')
    class Meta:
        abstract = True

class BaseWF(models.Model):
    wfstatus = models.IntegerField(
        db_column='WFSTATUS',
        blank=True,
        null=True,
        help_text='Kullanımda değil'
    )
    class Meta:
        abstract = True

class BaseBlocked(models.Model):
    blocked = models.SmallIntegerField(
        db_column='BLOCKED',
        blank=True,
        null=True,
        choices=[
            (0, 'Evet'),
            (1, 'Hayır')
        ],
        help_text='Bloke olmuş; 0 -> Evet, 1-> Hayır')
    class Meta:
        abstract = True

class BaseTextINC(models.Model):
    textinc = models.SmallIntegerField(
        db_column='TEXTINC',
        blank=True,
        null=True,
        choices=[
            (0, 'Hayır'),
            (1, 'Evet')
        ],
        help_text='Ayrıntılı açıklama')
    class Meta:
        abstract = True

class BaseAddress(models.Model):
    addr1 = models.CharField(db_column='ADDR1', max_length=201,
        blank=True, null=True, help_text='Adres satırı (1)')
    addr2 = models.CharField(db_column='ADDR2', max_length=201,
        blank=True, null=True, help_text='Adres satırı (2)')
    city = models.CharField(db_column='CITY', max_length=21,
        blank=True, null=True, help_text='Şehir')
    country = models.CharField(db_column='COUNTRY', max_length=21,
        blank=True, null=True, help_text='Ülke')
    postcode = models.CharField(db_column='POSTCODE', max_length=11,
        blank=True, null=True, help_text='Posta kodu')
    town = models.CharField(db_column='TOWN', max_length=51,
        blank=True, null=True, help_text='İlçe')
    district = models.CharField(db_column='DISTRICT', max_length=51,
        blank=True, null=True, help_text='Semt')

    """
    districtcode = models.CharField(db_column='DISTRICTCODE',
        max_length=13, blank=True, null=True, help_text='Semt kodu')
    towncode = models.CharField(db_column='TOWNCODE', max_length=13,
        blank=True, null=True, help_text='İlçe kodu')
    countrycode = models.CharField(db_column='COUNTRYCODE', max_length=13,
        blank=True, null=True, help_text='Ülke kodu')
    citycode = models.CharField(db_column='CITYCODE', max_length=13,
        blank=True, null=True, help_text='Şehir kodu')
    cityid = models.CharField(db_column='CITYID', max_length=9,
        blank=True, null=True)
    townid = models.CharField(db_column='TOWNID', max_length=18,
        blank=True, null=True)
    postlabelcode = models.CharField(db_column='POSTLABELCODE',
        max_length=101, blank=True, null=True)
    """
    class Meta:
        abstract = True


class LowLevelCodes10(models.Model):
    lowlevelcodes1 = models.IntegerField(db_column='LOWLEVELCODES1',
        blank=True, null=True)
    lowlevelcodes2 = models.IntegerField(db_column='LOWLEVELCODES2',
        blank=True, null=True)
    lowlevelcodes3 = models.IntegerField(db_column='LOWLEVELCODES3',
        blank=True, null=True)
    lowlevelcodes4 = models.IntegerField(db_column='LOWLEVELCODES4',
        blank=True, null=True)
    lowlevelcodes5 = models.IntegerField(db_column='LOWLEVELCODES5',
        blank=True, null=True)
    lowlevelcodes6 = models.IntegerField(db_column='LOWLEVELCODES6',
        blank=True, null=True)
    lowlevelcodes7 = models.IntegerField(db_column='LOWLEVELCODES7',
        blank=True, null=True)
    lowlevelcodes8 = models.IntegerField(db_column='LOWLEVELCODES8',
        blank=True, null=True)
    lowlevelcodes9 = models.IntegerField(db_column='LOWLEVELCODES9',
        blank=True, null=True)
    lowlevelcodes10 = models.IntegerField(db_column='LOWLEVELCODES10',
        blank=True, null=True)
    class Meta:
        abstract = True


class BaseVariable5(models.Model):
    variabledefs1 = models.CharField(db_column='VARIABLEDEFS1', max_length=251,
        blank=True, null=True)
    variabledefs2 = models.CharField(db_column='VARIABLEDEFS2', max_length=251,
        blank=True, null=True)
    variabledefs3 = models.CharField(db_column='VARIABLEDEFS3', max_length=251,
        blank=True, null=True)
    variabledefs4 = models.CharField(db_column='VARIABLEDEFS4', max_length=251,
        blank=True, null=True)
    variabledefs5 = models.CharField(db_column='VARIABLEDEFS5', max_length=251,
        blank=True, null=True)
    class Meta:
        abstract = True

class BaseVariable25(models.Model):
    variabledefs21 = models.CharField(db_column='VARIABLEDEFS21', max_length=251,
        blank=True, null=True)
    variabledefs22 = models.CharField(db_column='VARIABLEDEFS22', max_length=251,
        blank=True, null=True)
    variabledefs23 = models.CharField(db_column='VARIABLEDEFS23', max_length=251,
        blank=True, null=True)
    variabledefs24 = models.CharField(db_column='VARIABLEDEFS24', max_length=251,
        blank=True, null=True)
    variabledefs25 = models.CharField(db_column='VARIABLEDEFS25', max_length=251,
        blank=True, null=True)
    class Meta:
        abstract = True

class BaseVariable(models.Model):
    variabledefs1 = models.CharField(db_column='VARIABLEDEFS1', max_length=251,
        blank=True, null=True)
    variabledefs2 = models.CharField(db_column='VARIABLEDEFS2', max_length=251,
        blank=True, null=True)
    variabledefs3 = models.CharField(db_column='VARIABLEDEFS3', max_length=251,
        blank=True, null=True)
    variabledefs4 = models.CharField(db_column='VARIABLEDEFS4', max_length=251,
        blank=True, null=True)
    variabledefs5 = models.CharField(db_column='VARIABLEDEFS5', max_length=251,
        blank=True, null=True)
    variabledefs6 = models.CharField(db_column='VARIABLEDEFS6', max_length=251,
        blank=True, null=True)
    variabledefs7 = models.CharField(db_column='VARIABLEDEFS7', max_length=251,
        blank=True, null=True)
    variabledefs8 = models.CharField(db_column='VARIABLEDEFS8', max_length=251,
        blank=True, null=True)
    variabledefs9 = models.CharField(db_column='VARIABLEDEFS9', max_length=251,
        blank=True, null=True)
    variabledefs10 = models.CharField(db_column='VARIABLEDEFS10',
        max_length=251, blank=True, null=True)
    class Meta:
        abstract = True


class BaseGenexp(models.Model):
    genexp1 = models.CharField(db_column='GENEXP1', max_length=51, blank=True,
        null=True, help_text='Açıklama (1. satır)')
    genexp2 = models.CharField(db_column='GENEXP2', max_length=51, blank=True,
        null=True, help_text='Açıklama (2. satır)')
    genexp3 = models.CharField(db_column='GENEXP3', max_length=51, blank=True,
        null=True, help_text='Açıklama (3. satır)')
    genexp4 = models.CharField(db_column='GENEXP4', max_length=51, blank=True,
        null=True, help_text='Açıklama (4. satır)')
    genexp5 = models.CharField(db_column='GENEXP5', max_length=51, blank=True,
        null=True, help_text='Açıklama (5. satır)')
    genexp6 = models.CharField(db_column='GENEXP6', max_length=51, blank=True,
        null=True, help_text='Açıklama (6. satır)')

    class Meta:
        abstract = True

class BaseInfo(models.Model):
    created = models.DateTimeField(
        db_column='CAPIBLOCK_CREADEDDATE',
        null=True,
        blank=True,
        help_text='Oluşturulma'
    )
    updated = models.DateTimeField(
        db_column='CAPIBLOCK_MODIFIEDDATE',
        null=True,
        blank=True,
        help_text='Güncelleme'
    )
    created_by = models.ForeignKey(
        'L_CAPIUSER',
        db_column='CAPIBLOCK_CREATEDBY',
        null=True,
        blank=True,
        to_field='nr',
        on_delete=models.DO_NOTHING,
        related_name='%(app_label)s_%(class)s_created_by',
        help_text='Oluşturan'
    )
    updated_by = models.ForeignKey(
        'L_CAPIUSER',
        db_column='CAPIBLOCK_MODIFIEDBY',
        null=True,
        blank=True,
        to_field='nr',
        on_delete=models.DO_NOTHING,
        related_name='%(app_label)s_%(class)s_updated_by',
        help_text='Güncelleyen'
    )
    class Meta:
        abstract = True
