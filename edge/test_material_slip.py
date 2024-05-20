from load import unity
app = unity.UnityApplication()
app.Login("BTI", "3333", 20)


xml = """
<?xml version="1.0" encoding="ISO-8859-9"?>
<MATERIAL_SLIPS>
  <SLIP DBOP="INS" >
    <GROUP>3</GROUP>
    <TYPE>13</TYPE>
    <NUMBER>D.U_EMR_001</NUMBER>
    <DATE>18.04.2021</DATE>
    <TIME>65792</TIME>
    <TRANSACTIONS>
      <TRANSACTION>
        <ITEM_CODE>12.170.1610.0086</ITEM_CODE>
        <LINE_TYPE>0</LINE_TYPE>
        <QUANTITY>9</QUANTITY>
        <UNIT_CODE>ADET</UNIT_CODE>
        <UNIT_CONV1>1</UNIT_CONV1>
        <UNIT_CONV2>1</UNIT_CONV2>
      </TRANSACTION>
     </TRANSACTIONS>
    </SLIP>
</MATERIAL_SLIP>
"""


slip = app.NewDataObject(unity.constants.doMaterialSlip)
print("import", slip.ImportFromXmlStr('MATERIAL_SLIPS', xml))
if slip.Post() is False:
    print(slip.ValidateErrors)
