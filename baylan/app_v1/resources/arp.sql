SELECT 
  T.*, 
  case ISNULL(G.SözleşmeCariKodu, '0') when '0' then '0' else '1' end as 'ContractStatus' 
FROM 
  (
    SELECT 
      CLC.CODE 'CODE', 
      CLC.DEFINITION_ 'DEFINITION', 
      PAY.CODE 'PaymentPlanCode', 
      CLC.ACCEPTEINV, 
      PAY.DEFINITION_ 'PaymentPlanDefiniton', 
      ISNULL(PLN.DAY_, 0) 'PaymentPlanDay', 
      ACC.CODE 'AccCode', 
      CLC.INCHARGE 'Auth', 
      CLC.TELNRS1 'telephone', 
      CLC.FAXNR 'fax', 
      CLC.EMAILADDR 'email' 
    FROM 
      LG_${NS}_CLCARD CLC (NOLOCK) 
      LEFT OUTER JOIN LG_${NS}_PAYPLANS PAY (NOLOCK) ON CLC.PAYMENTREF = PAY.LOGICALREF 
      LEFT OUTER JOIN LG_${NS}_PAYLINES PLN (NOLOCK) ON PAY.LOGICALREF = PLN.PAYPLANREF 
      AND PLN.LINENO_ = 1 
      LEFT OUTER JOIN LG_${NS}_CRDACREF CRD (NOLOCK) ON CRD.CARDREF = CLC.LOGICALREF 
      AND CRD.TRCODE = 5 
      AND CRD.TYP = 1 
      LEFT OUTER JOIN LG_${NS}_EMUHACC ACC (NOLOCK) ON ACC.LOGICALREF = CRD.ACCOUNTREF 
    WHERE 
      CLC.ACTIVE = 0 
      AND PAY.ACTIVE = 0 
      AND PAY.CODE NOT LIKE 'X%' 
      ${WHERE}
  ) AS T 
  LEFT OUTER JOIN (
    select 
      CLC.CODE 'SözleşmeCariKodu' 
    from 
      LG_${NS}_PURCHOFFER POF (nolock) 
      LEFT OUTER JOIN LG_${NS}_CLCARD CLC (nolock) ON POF.CLIENTREF = CLC.LOGICALREF 
    WHERE 
      POF.POFFERENDDT >= GETDATE()-1 
      AND POFFERENDDT = (
        select 
          MAX (POFFERENDDT) 
        from 
          LG_${NS}_PURCHOFFER POR (nolock) 
          LEFT OUTER JOIN LG_${NS}_CLCARD CLC (nolock) ON POF.CLIENTREF = CLC.LOGICALREF 
        WHERE 
          POR.CLIENTREF = CLC.LOGICALREF
      ) 
    GROUP BY 
      CLC.CODE, 
      CLC.DEFINITION_, 
      POF.FICHENO, 
      POF.DATE_, 
      POFFERBEGDT, 
      POFFERENDDT
  ) AS G ON G.SözleşmeCariKodu = T.CODE 
ORDER BY 
  T.CODE
