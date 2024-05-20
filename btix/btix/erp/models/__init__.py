"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from .account import (
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

from .asset import (
    LG_FAREGIST,
    LG_FAYEAR
)

from .bank import (
    LG_BANKACC,
    LG_BNCARD,
    LG_BNFICHE,
    LG_BNTOTFIL,
    LG_BNFLINE
)

from .campaign import LG_CAMPAIGN

from .cash import (
    LG_KSCARD,
    LG_CSHTOTS,
    LG_KSLINES
)

from .cs import (
    LG_CSCARD,
    LG_CSROLL,
    LG_CSTRANS
)

from .current import (
    LG_CLCARD,
    LG_CLFICHE,
    LG_CLINTEL,
    LG_CLTOTFIL,
    LG_CLRNUMS,
    LG_CLFLINE
)

from .general import (
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
    LG_EBOOKDETAILDOC,
    LG_PROJECT,
)


from .inventory import (
    LG_SELCHVAL,
    LG_ITMBOMAS,
    LG_ITMCLSAS,
    LG_STINVTOT,
    LG_ITMFACTP,
    LG_INVDEF,
    LG_CHARASGN,
    LG_CHARCODE,
    LG_CHARVAL,
    LG_ITEMS,
    LG_ITEMSUBS,
    LG_SERILOTN,
    LG_SLTRANS,
    LG_STCOMPLN,
    LG_STINVENS,
    LG_SUPPASGN,
    LG_ITMUNITA,
    LG_UNITBARCODE
)


from .production import (
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

from .quality import (
    LG_QASGN,
    LG_QCLVAL,
    LG_SLQCASGN,
    LG_QCSET,
    LG_QCSLINE
)

from .sales import (
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
    LG_TOOLREQ,
    LG_EARCHIVEDET,
)

from .stock import (
    LG_STFICHE,
    LG_INVOICE,
    LG_SRVTOT,
    LG_ORFICHE,
    LG_ORFLINE,
    LG_PRODUCER,
    LG_STLINE,
    LG_SRVNUMS
)

from .system import (
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

from .trade import (
    LG_ASCOND,
    LG_DECARDS,
    LG_DEMANDFICHE,
    LG_DEMANDPEGGING,
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

from .unit import (
    LG_UNITSETF,
    LG_UNITSETL,
    LG_SRVUNITA,
    LG_UNITSETC
)


from .wf import LG_WFTASK
