"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""
import io
import base64
from zipfile import ZipFile

import zeep
from zeep.plugins import HistoryPlugin


class Elogo:
    wsdl = 'https://pb.elogo.com.tr/PostBoxService.svc?singlewsdl'
    def __init__(self, username, pwd):
        self.username = username
        self.pwd = pwd
        self.history = HistoryPlugin()

        self.client = zeep.Client(wsdl=self.wsdl)
        self.logged = False
        self.sid = None

    def login(self):
        resp = self.client.service.Login(login={
            'passWord': self.pwd,
            'userName': self.username
        })
        if resp and resp['LoginResult']:
            self.sid = resp['sessionID']
            self.logged = True
        else:
            self.sid = None
            self.logged = False

    def logout(self):
        resp = self.client.service.Logout(
            sessionID=self.sid
        )
        return resp

    def get_document_data(self, uuid, doc_type='EARCHIVE', dformat='PDF'):
        if self.logged:
            data_type = self.client.get_type('ns5:GetDocumentType')(dformat)

            return self.client.service.getDocumentData(
                sessionID=self.sid,
                uuid=uuid,
                docType=doc_type,
                dataType=data_type
            )
        return None

    def document_data_convert_to_bytes(self, document, keys=['binaryData', 'Value']):
        doc = document
        for key in keys:
            doc = doc[key]
        return io.BytesIO(doc).getvalue()

    def extract_from_zip(self, guid, bind):
        with ZipFile(io.BytesIO(bind)) as zipf:
            return zipf.read(f'{guid}.pdf')

    def get_encoded_pdf(self, document, guid):
        bind = self.document_data_convert_to_bytes(document)
        pdf = self.extract_from_zip(guid, bind)
        return self.convert_bin_to_base64(pdf)

    def convert_bin_to_base64(self, bin):
        return base64.b64encode(bin).decode()

    def validate_gib(self, vkn):
        if self.logged:
            checker = self.client.service.GetValidateGIBUser(
                sessionID=self.sid,
                paramList=[f'VKN={vkn}']
            )
            if checker and (checker['resultCode'] == 1 and
                checker['errorCode'] == 0):
                resp = checker['outputList']['string']
                return {r.split('=', 1)[0]: r.split('=', 1)[1] for r in resp}
        return None
    
    def checkGibUser(self, vkn):
        if self.logged:
            users = self.client.service.CheckGibUser(
                sessionID=self.sid,
                vknTcknList=[vkn]
            )

            if users and users['CheckGibUserResult']:
                result_code = users['CheckGibUserResult']['resultCode']
                result_msg = users['CheckGibUserResult']['resultMsg']

                response_data = {
                    'resultCode': result_code,
                    'resultMsg': result_msg,
                }
               
                if users['userList'] and users['userList']['GibUserType']:
                    if users['userList']['GibUserType'][0]['DespatchAdviceGbList']:
                        if users['userList']['GibUserType'][0]['DespatchAdviceGbList']['GibUserInfoType'][0]:
                            gib_user_info = users['userList']['GibUserType'][0]['DespatchAdviceGbList']['GibUserInfoType'][0]
                            response_data['userList'] = {
                                'Alias': gib_user_info['Alias'],
                                'FirstCreationTime': gib_user_info['FirstCreationTime'],
                                'Identifier': gib_user_info['Identifier'],
                                'Title': gib_user_info['Title'],
                                'Type': gib_user_info['Type'],
                            }

                            return response_data
                        return None
                    return None
        return None

    def gibUserInfo(self,vkn):

        if self.logged:
            checker = self.client.service.GetValidateGIBUser(
                sessionID=self.sid,
                paramList=[f'VKN={vkn}']
            )

            if checker and (checker['resultCode'] == 1 and
                checker['errorCode'] == 0):
                    return checker

            return None
        return None