"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.test import TestCase

class QueryTest(TestCase):
    databases = '__all__'
    def test_account(self):
        from erp.models import (
            LG_EMUHACC,
            LG_ACCCODES,
            LG_CRDACREF,
            LG_EMFICHE,
            LG_LOGREP,
            LG_EMUHTOT,
            LG_EMFLINE,
            LG_ADDTAX,
            LG_ADDTAXLINE
        )
        LG_EMUHACC.objects.filter()
        LG_ACCCODES.objects.filter()
        LG_CRDACREF.objects.filter()
        LG_EMFICHE.objects.filter()
        LG_LOGREP.objects.filter()
        LG_EMUHTOT.objects.filter()
        LG_EMFLINE.objects.filter()
        LG_ADDTAX.objects.filter()
        LG_ADDTAXLINE.objects.filter()

    def test_asset(self):
        from erp.models import LG_FAREGIST, LG_FAYEAR
        LG_FAREGIST.objects.filter()
        LG_FAYEAR.objects.filter()

    def test_bank(self):
        from erp.models import (
            LG_BANKACC,
            LG_BNCARD,
            LG_BNFICHE,
            LG_BNTOTFIL,
            LG_BNFLINE
        )
        LG_BANKACC.objects.filter()
        LG_BNCARD.objects.filter()
        LG_BNFICHE.objects.filter()
        LG_BNTOTFIL.objects.filter()
        LG_BNFLINE.objects.filter()

    def test_campaign(self):
        from erp.models import LG_CAMPAIGN
        LG_CAMPAIGN.objects.filter()

    def test_cash(self):
        from erp.models import (
            LG_KSCARD,
            LG_CSHTOTS,
            LG_KSLINES
        )
        LG_KSCARD.objects.filter()
        LG_CSHTOTS.objects.filter()
        LG_KSLINES.objects.filter()

    def test_cs(self):
        from erp.models import (
            LG_CSCARD,
            LG_CSROLL,
            LG_CSTRANS
        )
        LG_CSCARD.objects.filter()
        LG_CSROLL.objects.filter()
        LG_CSTRANS.objects.filter()

    def test_current(self):
        from erp.models import (
            LG_CLCARD,
            LG_CLFICHE,
            LG_CLINTEL,
            LG_CLTOTFIL,
            LG_CLRNUMS,
            LG_CLFLINE
        )
        LG_CLCARD.objects.filter()
        LG_CLFICHE.objects.filter()
        LG_CLINTEL.objects.filter()
        LG_CLTOTFIL.objects.filter()
        LG_CLRNUMS.objects.filter()
        LG_CLFLINE.objects.filter()

    def test_general(self):
        from erp.models import (
            LG_FOLDER,
            LG_EMGRPASS,
            LG_EMPGROUP,
            LG_EMPLOYEE,
            LG_ENGCLINE,
            LG_FIRMDOC,
            LG_LABORREQ,
            LG_LNGEXCSETS,
            LG_TRANSAC,
            LG_PRDCOST,
            LG_SHIPINFO,
            LG_TRGPAR,
            LG_PROJECT
        )
        LG_FOLDER.objects.filter()
        LG_EMGRPASS .objects.filter()
        LG_EMPGROUP.objects.filter()
        LG_EMPLOYEE.objects.filter()
        LG_ENGCLINE.objects.filter()
        LG_FIRMDOC.objects.filter()
        LG_LABORREQ.objects.filter()
        LG_LNGEXCSETS.objects.filter()
        LG_TRANSAC.objects.filter()
        LG_PRDCOST.objects.filter()
        LG_SHIPINFO.objects.filter()
        LG_TRGPAR.objects.filter()
        LG_PROJECT.objects.filter()

    def test_inventory(self):
        from erp.models import (
            LG_SELCHVAL,
            LG_ITMBOMAS,
            LG_ITMCLSAS,
            LG_STINVTOT,
            LG_ITMFACTP,
            LG_INVDEF,
            LG_CHARASGN,
            LG_CHARCODE,
            LG_CHARVAL ,
            LG_ITEMS,
            LG_ITEMSUBS,
            LG_SERILOTN,
            LG_SLTRANS,
            LG_STCOMPLN,
            LG_STINVENS,
            LG_SUPPASGN,
            LG_ITMUNITA
        )

        LG_SELCHVAL.objects.filter()
        LG_ITMBOMAS.objects.filter()
        LG_ITMCLSAS.objects.filter()
        LG_STINVTOT.objects.filter()
        LG_ITMFACTP.objects.filter()
        LG_INVDEF.objects.filter()
        LG_CHARASGN.objects.filter()
        LG_CHARCODE.objects.filter()
        LG_CHARVAL .objects.filter()
        LG_ITEMS.objects.filter()
        LG_ITEMSUBS.objects.filter()
        LG_SERILOTN.objects.filter()
        LG_SLTRANS.objects.filter()
        LG_STCOMPLN.objects.filter()
        LG_STINVENS.objects.filter()
        LG_SUPPASGN.objects.filter()
        LG_ITMUNITA.objects.filter()

    def test_production(self):
        from erp.models import (
            LG_ACTIVITYAMNT,
            LG_WSGRPF,
            LG_WSGRPASS,
            LG_PRVOPASG,
            LG_PRODORD,
            LG_PEGGING,
            LG_BOMASTER,
            LG_BOMLINE,
            LG_BOMPARAM,
            LG_COPRDBOM,
            LG_ROUTING,
            LG_RTNGLINE,
            LG_DISPLINE,
            LG_WORKSTAT,
            LG_WSATTASG,
            LG_WSATTVAS,
            LG_WSCHCODE,
            LG_WSCHVAL
        )
        LG_ACTIVITYAMNT.objects.filter()
        LG_WSGRPF.objects.filter()
        LG_WSGRPASS.objects.filter()
        LG_PRVOPASG.objects.filter()
        LG_PRODORD.objects.filter()
        LG_PEGGING.objects.filter()
        LG_BOMASTER.objects.filter()
        LG_BOMLINE.objects.filter()
        LG_BOMPARAM.objects.filter()
        LG_COPRDBOM.objects.filter()
        LG_ROUTING.objects.filter()
        LG_RTNGLINE.objects.filter()
        LG_DISPLINE.objects.filter()
        LG_WORKSTAT.objects.filter()
        LG_WSATTASG.objects.filter()
        LG_WSATTVAS.objects.filter()
        LG_WSCHCODE.objects.filter()
        LG_WSCHVAL.objects.filter()

    def test_quality(self):
        from erp.models import (
            LG_QASGN,
            LG_QCLVAL,
            LG_SLQCASGN,
            LG_QCSET,
            LG_QCSLINE
        )
        LG_QASGN.objects.filter()
        LG_QCLVAL.objects.filter()
        LG_SLQCASGN.objects.filter()
        LG_QCSET.objects.filter()
        LG_QCSLINE.objects.filter()

    def test_sales(self):
        from erp.models import (
            LG_CONTACTS,
            LG_DISTLINE,
            LG_DISTTEMP,
            LG_LNOPASGN,
            LG_LOCATION,
            LG_OPERTION,
            LG_OPRTREQ,
            LG_OPATTASG,
            LG_ACTPEPL,
            LG_ROUTETRS,
            LG_ROUTE,
            LG_SLSMAN,
            LG_SLSCLREL,
            LG_TARGETS,
            LG_TOOLREQ
        )
        LG_CONTACTS.objects.filter()
        LG_DISTLINE.objects.filter()
        LG_DISTTEMP.objects.filter()
        LG_LNOPASGN.objects.filter()
        LG_LOCATION.objects.filter()
        LG_OPERTION.objects.filter()
        LG_OPRTREQ.objects.filter()
        LG_OPATTASG.objects.filter()
        LG_ACTPEPL.objects.filter()
        LG_ROUTETRS.objects.filter()
        LG_ROUTE.objects.filter()
        LG_SLSMAN.objects.filter()
        LG_SLSCLREL.objects.filter()
        LG_TARGETS.objects.filter()
        LG_TOOLREQ.objects.filter()

    def test_stock(self):
        from erp.models import (
            LG_STFICHE,
            LG_INVOICE,
            LG_SRVTOT,
            LG_ORFICHE,
            LG_ORFLINE,
            LG_PRODUCER,
            LG_STLINE,
            LG_SRVNUMS
        )
        LG_STFICHE.objects.filter()
        LG_INVOICE.objects.filter()
        LG_SRVTOT.objects.filter()
        LG_ORFICHE.objects.filter()
        LG_ORFLINE.objects.filter()
        LG_PRODUCER.objects.filter()
        LG_STLINE.objects.filter()
        LG_SRVNUMS.objects.filter()

    def test_system(self):
        from erp.models import (
            L_COUNTRY,
            L_CITY,
            L_TOWN,
            L_DISTRICT,
            L_POSTCODE,
            L_BANKCODE,
            L_BNBRANCH,
            LG_CATEGLISTS,
            L_CURRENCYLIST,
            L_CURRENCYPARS,
            L_CAPIDEPT,
            L_CAPIDIV,
            L_LDOCNUM,
            L_DAILYEXCHANGES,
            L_CAPIFACTORY,
            L_CAPIFACTDIV,
            L_CAPIFIRM,
            L_FIRMPARAMS,
            L_CAPIGROUP,
            LG_HISTORY,
            L_CAPIUSER,
            L_GOUSERS,
            L_NET,
            L_CAPIPERIOD,
            L_DYNREP,
            L_DYNREPUSRR,
            L_CAPIROLE,
            L_SHPAGENT,
            L_SHPTYPES,
            LG_USAGESTAT,
            L_STATUSINFO,
            L_CAPITERMINAL,
            L_TRADGRP,
            L_CAPIUNIT,
            L_CAPIVERS,
            L_CAPIWHOUSE
        )
        L_COUNTRY.objects.filter()
        L_CITY.objects.filter()
        L_TOWN.objects.filter()
        L_DISTRICT.objects.filter()
        L_POSTCODE.objects.filter()
        L_BANKCODE.objects.filter()
        L_BNBRANCH.objects.filter()
        LG_CATEGLISTS.objects.filter()
        L_CURRENCYLIST.objects.filter()
        L_CURRENCYPARS.objects.filter()
        L_CAPIDEPT.objects.filter()
        L_CAPIDIV.objects.filter()
        L_LDOCNUM.objects.filter()
        L_DAILYEXCHANGES.objects.filter()
        L_CAPIFACTORY.objects.filter()
        L_CAPIFACTDIV.objects.filter()
        L_CAPIFIRM.objects.filter()
        L_FIRMPARAMS.objects.filter()
        L_CAPIGROUP.objects.filter()
        LG_HISTORY.objects.filter()
        L_CAPIUSER.objects.filter()
        L_GOUSERS.objects.filter()
        L_NET.objects.filter()
        L_CAPIPERIOD.objects.filter()
        L_DYNREP.objects.filter()
        L_DYNREPUSRR.objects.filter()
        L_CAPIROLE.objects.filter()
        L_SHPAGENT.objects.filter()
        L_SHPTYPES.objects.filter()
        LG_USAGESTAT.objects.filter()
        L_STATUSINFO.objects.filter()
        L_CAPITERMINAL.objects.filter()
        L_TRADGRP.objects.filter()
        L_CAPIUNIT.objects.filter()
        L_CAPIVERS.objects.filter()
        L_CAPIWHOUSE.objects.filter()

    def test_trade(self):
        from erp.models import (
            LG_ASCOND,
            LG_DECARDS,
            LG_DEMANDLINE,
            LG_EMCENTER,
            LG_PAYLINES,
            LG_PAYPLANS,
            LG_PRCARDS,
            LG_PRCLIST,
            LG_PAYTRANS,
            LG_SPECODES,
            LG_SRVCARD
        )
        LG_ASCOND.objects.filter()
        LG_DECARDS.objects.filter()
        LG_DEMANDLINE.objects.filter()
        LG_EMCENTER.objects.filter()
        LG_PAYLINES.objects.filter()
        LG_PAYPLANS.objects.filter()
        LG_PRCARDS.objects.filter()
        LG_PRCLIST.objects.filter()
        LG_PAYTRANS.objects.filter()
        LG_SPECODES.objects.filter()
        LG_SRVCARD.objects.filter()

    def test_unit(self):
        from erp.models import (
            LG_UNITSETF,
            LG_UNITSETL,
            LG_SRVUNITA,
            LG_UNITSETC
        )
        LG_UNITSETF.objects.filter()
        LG_UNITSETL.objects.filter()
        LG_SRVUNITA.objects.filter()
        LG_UNITSETC.objects.filter()

    def test_Wf(self):
        from erp.models import (
            LG_WFTASK
        )
        LG_WFTASK.objects.filter()