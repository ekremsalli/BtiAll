import os
import subprocess
import win32serviceutil
from datetime import datetime
services = [
    #'SenihaIdeaSoftIntegrationService'
]

path = r'C:\\Program Files (x86)\\LOGO\\TIGER3'
cmd = r's_REGISTER.bat'
logo_bin = r'C:\Program Files (x86)\LOGO\TIGER3\Tiger3.exe'

app_path = r'C:\\inetpub\\api'


from win32com.client import gencache
unity = gencache.EnsureModule('{51F6657D-9972-45FD-8D5D-98849802A9C9}', 0, 1, 0)

try:
    app = unity.UnityApplication()
    app.Login('LOGO', 'LOGO', 1)
except:
    with open('history.dat', 'a+') as f:
        info = f'{datetime.now()} registering object...\n'
        f.write(info)


    try:
        print('killing task LOBJECTS.exe')
        os.system('taskkill /im LOBJECTS.exe /T /F')
    except:
        pass



    try:
        print('Calling s_REGISTER.bat')
        subprocess.check_call([cmd], cwd=path)
    except:
        pass

    try:
        print('Registering LOBJECTS.dll!')
        subprocess.check_call([r'regsvr32 LOBJECTS.dll /u'], cwd=path)
        subprocess.check_call([r'regsvr32 LOBJECTS.dll'], cwd=path)
        for service in services:
            win32serviceutil.StopService(service)
            win32serviceutil.StartService(service)
        #subprocess.check_call([r'python manage.py logo_rest_tokens'], cwd=app_path)
    except:
        pass
    #subprocess.Popen(logo_bin)
