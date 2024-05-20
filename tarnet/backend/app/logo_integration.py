import requests
import base64
import json

from common.settings import TK_LOGO_SERVER_ADDRESS
from common.settings import LOGO_USERNAME
from common.settings import LOGO_PASSWORD
from common.settings import LOGO_CLIENT_TOKEN
from common.settings import LOGO_FIRM_NO


class LogoApi:
    SERVER_ADDRESS = TK_LOGO_SERVER_ADDRESS
    USERNAME = LOGO_USERNAME
    PASSWORD = LOGO_PASSWORD
    CLIENT_TOKEN = LOGO_CLIENT_TOKEN
    FIRM_NO = LOGO_FIRM_NO

    @staticmethod
    def get_auth_token(username, password, client_token, firm, url, lang="TRTR"):
        """
        Logo ya login olduktan sonra auth token döndürür
        """
        text = f"{username}:{password}:{client_token}:{firm}:{lang}"
        auth = base64.b64encode(text.encode("utf-8")).decode("utf-8")
        headers = {
            'Authorization': f"Basic {auth}",
            'Content-Type': 'application/json'
        }
        URL = f"{url}/restservices/rest/login"
        response = requests.post(url=URL, data={}, headers=headers)

        if response.status_code == 200:
            result = response.json()
            r = result.get("authToken")
            return r
        return {
            "status_code": f"Login Erorr {response.status_code}"
        }

    @staticmethod
    def send_logo(url, client_token, auth_token, param, user):
        """
        Arman api den filtrelenen data yı logoya gönderir
        """
        text = f"{client_token}:{auth_token}:{user}"
        auth = base64.b64encode(text.encode("utf-8")).decode("utf-8")
        payload = {}
        files = {}
        headers = {
            'auth-token': f"{auth}",
            'accept': 'application/json'
        }
        params = {
            "className": """%7BBTI-TarimKredi-15B-3BA3-2D105AAFDC37%7D.com.bti.server.HRWebService""",
            "methodName": "setPntHeader",
            "parameters": f"""{param}"""
        }
        URL = f"{url}/restservices/rest/customization/invokeMethod?className={params.get('className')}&methodName={params.get('methodName')}&parameters={params.get('parameters')}"

        response = requests.request(
            "POST", url=URL, headers=headers, data=payload, files=files)
        result = response.json()
        return result

    @staticmethod
    def data_to_string(data, start_date):
        """
        verileri logoya göndermek için stringe çevirir
        """
        unique_ids = set()
        for i in range(len(data)):
            unique_ids.add(data[i]["unique_id"])

        text_list = []
        for x in unique_ids:
            for y in range(len(data)):
                if x == data[y].get("unique_id"):
                    if f"{start_date.split('-')[0]}-{start_date.split('-')[1]}" == f"""{data[y].get("utc").split('-')[0]}-{data[y].get("utc").split('-')[1]}""":
                        text = f"""{x},{start_date.split('-')[0]},{start_date.split('-')[1]},{data[y].get("utc").split('-')[2]};{data[y].get("in_time")};{data[y].get("out_time")}"""
                        text_list.append(text)

        str_list = []
        for a in unique_ids:
            text1 = f"""%5B '{a}','{start_date.split('-')[0]}','{start_date.split('-')[1]}','"""
            for i in range(len(text_list)):
                if text_list[i].split(",")[0] == a and text_list[i].split(",")[1] == start_date.split('-')[0] and \
                        text_list[0].split(",")[2] == \
                        start_date.split('-')[1]:
                    text1 += f"""{text_list[i].split(",")[3]};"""

            t2 = text1.rstrip(";")
            t2 += "' %5D"
            obj = {
                "unique_id": a,
                "query_text": t2,
                "start_date": start_date
            }
            str_list.append(obj)
        return str_list

 
