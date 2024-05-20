import requests

class Arvato:
    def __init__(self, base_url, user, pwd):
        self.base_url = base_url
        self.user = user
        self.pwd = pwd
        self.token = None

    @property
    def default_headers(self):
        headers = {
            'Content-Type': 'application/json'
        }
        if self.token:
            headers.update({
                'token': self.token
            })
        return headers

    def _request(self, type, url, params=None,
        headers={}, data=None, json=None, timeout=15):
        dheaders = self.default_headers
        dheaders.update(headers)
        return requests.api.request(
            type,
            url,
            params=params,
            headers=dheaders,
            data=data,
            json=json,
            timeout=timeout
        )

    def cancel_order(self, data):
        url = f"{self.base_url}/OutBoundOrder/CancelOrder"
        result = self._request('POST', url, json=data)
        return result.json()

    def add_outbound_order(self, data):
        url = f"{self.base_url}/OutBoundOrder/Add"
        result = self._request('POST', url, json=data)
        return result.json()

    def generate_token(self):
        url = f"{self.base_url}/Common/Authenticate"
        result = self._request('POST', url, json={
            'userName': self.user,
            'password': self.pwd
        })
        if result.status_code == 200:
            resp = result.json()
            if 'data' in resp and 'token' in resp['data']:
                self.token = resp['data']['token']
                return True
        raise Exception('Token alınamadı!')


if __name__ == '__main__':
    arvato = Arvato(
        'https://testslotservices.arvatoscm.com.tr/extapi',
        'demouser',
        'demopassword'
    )
    if arvato.generate_token():
        print(arvato.token)
