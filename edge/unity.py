from win32com.client import gencache
import pythoncom

unity = gencache.EnsureModule('{51F6657D-9972-45FD-8D5D-98849802A9C9}', 0, 1, 0)
app = unity.UnityApplication()

print(app.Login("BTI", "3333", 20))
import time
while True:
    try:
        print("is connected?", app.Connected)
        record = app.NewDataObject(unity.constants.doSalesInvoice)
        print(record.Read(6646))
    except pythoncom.com_error as error:
        hr, _, _, _ = error.args
        print(hr)
        if hr == -2147023174:
            app = unity.UnityApplication()
            app.Login("BTI", "3333", 20)
            print("reloaded...")

    time.sleep(10)
    


"""
print(app.Disconnect())
# veya

print(app.Connect())
print(app.Connected) # is connected?
print(app.UserLogin("BTI", "3333"))
#print(app.UserLoggedIn()) # is logged in?
print(app.CompanyLogin(20, 1))
print(app.CompanyLoggedIn)

print(app.CompanyLogout())
print("company logged in?", app.CompanyLoggedIn)

print(app.UserLogout())
#print("user logged in", app.UserLoggedIn)
print(app.Disconnect())
print("app connected", app.Connected)
"""
# lines.AddSeriLots() - lines.DeleteLine() - lines.GetStockLinePrice()

# data.FillAccCodes() - data.ApplyCampaign() - data.ExportToXML()

# data.Post() - dara.ReCalculate()

# data.New(), data.Read(<ref>) data.Delete(<ref>)
# data.Post() false donerse!
# data.ErrorCode != 0
# data.Post() -> data.ErrorDesc, data.DBErrorDesc,
# data.ValidateErrors.Count -> data.ValidateError[i].ID.ToString() / data.ValidateError[i].Error.ToString()
data = app.NewDataObject(unity.constants.doMaterialSlip)
data.New()


print(app.GetLastErrorString())
 
