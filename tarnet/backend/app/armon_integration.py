"""
Armon api den veri çekilecek fonksiyonlar burda bulunur
"""
import requests
import json

from common.settings import ARMON_SERVER_ADDRESS
from common.settings import ARMON_USERNAME
from common.settings import ARMON_PASSWORD


class ArmonApi:
    SERVER_ADDRESS = ARMON_SERVER_ADDRESS
    USERNAME = ARMON_USERNAME
    PASSWORD = ARMON_PASSWORD

    @staticmethod
    def get_grand_type_id(username: str):
        """
        Token almak için grant_type_id döndürür
        """
        data = {"username": username}
        urls = f"{ArmonApi.SERVER_ADDRESS}/auth/user"
        response = requests.post(url=urls, data=data)

        if response.status_code == 200:
            response = response.json()
            result = response.get("organizations")
            return result
        return {"status": response.status_code,
                "Error": f"{urls} hata!!!!"}

    @staticmethod
    def get_token(grant_type_id: str, username: str, password: str):
        """
        kullanıcı ya göre token ve organization_id döndürür
        """
        data = {
            "username": username,
            "password": password}

        urls = f"{ArmonApi.SERVER_ADDRESS}/auth/usernamepass/{grant_type_id}"
        response = requests.post(url=urls, data=data)

        if response.status_code == 200:
            response = response.json()
            result = {
                "organization_id": response.get("organization").get("organization").get("id"),
                "token": response.get("token")
            }
            return result
        return {"status": response.status_code,
                "Error": f"{urls} hata !!!!"}

    @staticmethod
    def data_filter(data, organization_id):
        """
        Armon api den gelen verileri filtreler
      """
        first_list = []
        for i in range(len(data)):
            if data[i] is not None and data[i]["id"] is not None:
                if data[i]["identity"] is not None:
                    obj = {
                        "organization_id": organization_id,
                        "tarnet_user_id": data[i]["identity"]["id"],
                        "unique_id": data[i]["identity"]["uniqueId"],
                        "full_name": f"{data[i]['identity']['name']} {data[i]['identity']['surname']}",
                        "utc": data[i]["utc"],
                    }
                    if data[i]["direction"] == 1:
                        obj.update({
                            "in_time": data[i]["utc"],
                            "out_time": None,
                            "direction": data[i]["direction"]
                        })
                    elif data[i]["direction"] == 2:
                        obj.update({
                            "in_time": None,
                            "out_time": data[i]["utc"],
                            "direction": data[i]["direction"]
                        })
                    else:
                        obj.update({
                            "in_time": None,
                            "out_time": None,
                            "direction": data[i]["direction"]
                        })
                    first_list.append(obj)
        return first_list

    @staticmethod
    def organization_users_log(token, organization_id, start_date, end_date):
        """
        Organizasyona ait Personellerin işe giriş - çıkış saatlerini listeler
        """
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"
        }
        body = {
            "startUtc": start_date,
            "endUtc": end_date,
            "take": 10000000000000,
            "returnTotalCount": True,
            "sortDateDesc": True
        }
        url = f"{ArmonApi.SERVER_ADDRESS}/u/v1/{organization_id}/report/accesslogs/v2"
        response = requests.post(url=url, headers=headers, data=json.dumps(body))

        if response.status_code == 200:
            response = response.json()
            data = response.get("items")
            data_filter = ArmonApi.data_filter(data, organization_id)
            return data_filter
        return response.status_code
