"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from erp.transport import API


class Image(API):
    def __init__(self, doctype, logref, index, *args, **kwargs):
        if doctype not in [0, 30]:
            raise Exception('Geçersiz dokuman tipi!')

        self.doctype = doctype
        self.logref = logref
        if index not in [1, 2]:
            raise Exception('Geçersiz indeks!')

        self.index = index

        super().__init__(*args, **kwargs)

    def get(self):
        method = 'methods/ExportBase64EncodedImage'

        self.endpoint = f'{method}/{self.doctype}/{self.logref}/{self.index}'

        request = self.request('GET')

        if request.status_code == 200:
            return request.text[1:-1]

        return request

    def post(self, itype, data):
        if itype not in [1,2,3]:
            # 1 = Bitmap (bmp)
            # 2 = JPEG (jpg)
            # 3 = PNG (png)
            raise Exception('Geçersiz resim formatı!')

        method = 'methods/ImportBase64EncodedImage'

        self.endpoint = f'{method}/{self.doctype}/{self.logref}/{itype}/{self.index}/'
        request = self.request('POST', json={
            'base64EncodedImage': data
        })

        return request


class ImageXML(API):
    def upload(self, doctype, logref, itype, index, image):
        self.xml_endpoint = ''

        data = {
            'doctype': doctype,
            'logref': logref,
            'itype': itype,
            'index': index,
            'image': image
        }

        cmd = {
            'do': 'ImportImage',
            'pid': self.pid,
            'token': self.generate_xml_token(),
            'user': self.user,
            'data': data
        }

        return self.send_to_edge(cmd)
