SELECT
  --TOP 500
  ITM.ACTIVE, 
  ITM.LOGICALREF, 
  ITM.CODE, 
  ITM.NAME, 
  ITM.VAT, 
  SETL.CODE AS MAINCODE, 
  AC.CODE AS GLCODE, 
  ITM.CARDTYPE, 
  ISNULL(CR.TYP, 0) AS GLTYP
FROM 
  LG_${NS}_ITEMS ITM 
  LEFT JOIN LG_${NS}_CRDACREF CR WITH (NOLOCK) ON ITM.LOGICALREF = CR.CARDREF 
  AND CR.TRCODE = 1 
  LEFT JOIN LG_${NS}_EMUHACC AC WITH (NOLOCK) ON AC.LOGICALREF = CR.ACCOUNTREF 
  LEFT OUTER JOIN LG_${NS}_UNITSETL SETL ON SETL.UNITSETREF = ITM.UNITSETREF 
  AND SETL.LINENR = 1 
WHERE 
  ITM.CARDTYPE NOT IN (4, 22) 
  ${WHERE}