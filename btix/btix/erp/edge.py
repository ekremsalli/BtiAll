"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

import zmq
import json

from django.conf import settings
from erp.active import Active
from bti.models.flow import Flow

class Edge:

    @classmethod
    def generate_pid(cls):
        return Flow.generate_pid()

    @classmethod
    def generate_token(cls, pid):
        from hashlib import md5
        payload = f"{Active.xml_secret}*{pid}"
        return md5(payload.encode("utf-8")).hexdigest()

    def __init__(self):
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REQ)

    def connect(self):
        self.socket.connect(Active.xml_server)
        self.socket.setsockopt(zmq.RCVTIMEO, settings.XML_CLIENT_TIMEOUT)        

    def disconnect(self):
        try:
            self.socket.close()
        except Exception as e:
            print(e)
    
    def send(self, cmd, *args, **kwargs):
        if 'ignore_pid_check' in kwargs and kwargs.get('ignore_pid_check'):
            cmd['ignore_pid_check'] = kwargs.get('ignore_pid_check')            
        self.socket.send_string(json.dumps(cmd))
        response = json.loads(self.socket.recv_string())        
        return response

    def __del__(self):
        try:
            self.socket.close()
        except Exception as e:
            print(e)


