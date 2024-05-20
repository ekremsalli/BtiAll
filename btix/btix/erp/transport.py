"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from datetime import datetime
import json

from requests import request
import zmq

from django.conf import settings
from erp.auth import Token, Auth
from erp.active import Active
from bti.models.flow import Flow

from django.core.serializers.json import DjangoJSONEncoder

import logging

logger = logging.getLogger("erp")

class API:
    def __init__(self, *args, pid=None, prev_flow=None, **kwargs):
        self.xml = kwargs.get('xml', '')
        self.data = kwargs.get("data", {})
        self.is_partial = kwargs.get('partial', False)
        self.instance = None
        self.meta = None
        if hasattr(self, "serializer_class"):
            self.instance = self.serializer_class(
                data=self.data, partial=self.is_partial)
            meta = self.serializer_class.Meta
            self.meta = meta
            if hasattr(meta, "DATA_OBJECT"):
                self.xml_endpoint = meta.DATA_OBJECT
            if hasattr(meta, "REST_ENDPOINT"):
                self.endpoint = meta.REST_ENDPOINT

        if "endpoint" in kwargs:
            self.endpoint = kwargs.get('endpoint')
        if "xml_endpoint" in kwargs:
            self.xml_endpoint = kwargs.get('xml_endpoint')
        self.user = kwargs.get("user", "")
        if pid is None:
            pid = Flow.generate_pid()
        self.pid = pid
        self.prev_flow = prev_flow
        self.skip_flow = kwargs.get('skip_flow', False)
        self.keyword1 = kwargs.get('keyword1', None)
        self.keyword2 = kwargs.get('keyword2', None)
        self.keyword3 = kwargs.get('keyword3', None)

    def is_valid(self, raise_exception=True):
        if self.instance is None:
            raise Exception('Instance tanımlanmamış!')
        return self.instance.is_valid(raise_exception=raise_exception)

    def get_data(self, **kwargs):
        return self.data

    def set_data(self, data):
        self.data = data

    def set_user(self, user):
        self.user = user

    def get_xml(self):
        return self.xml

    def set_xml(self, xml):
        self.xml = xml

    def set_endpoint(self, endpoint):
        self.endpoint = endpoint

    def retrieve(self, *args, **kwargs):
        return self._get(*args, **kwargs)

    def update(self, pk, *args, **kwargs):
        return self._put(*args, suffix=pk, **kwargs)

    def partial_update(self, pk, *args, **kwargs):
        return self._patch(*args, suffix=pk, **kwargs)

    def destroy(self, *args, **kwargs):
        return self._delete(*args, **kwargs)

    def create(self, *args, **kwargs):
        return self._post(*args, **kwargs)

    def _get(self, *args, **kwargs):
        return self.call('GET', *args, **kwargs)

    def _put(self, *args, **kwargs):
        return self.call('PUT', *args, **kwargs)

    def _patch(self, *args, **kwargs):
        return self.call('PATCH', *args, **kwargs)

    def _delete(self, *args, **kwargs):
        return self.call('DELETE', *args, **kwargs)

    def _post(self, *args, **kwargs):
        return self.call('POST', *args, **kwargs)

    def call(self, method, *args, **kwargs):
        start = datetime.now()
        try:
            request = self.request(
                method,
                *args,
                **kwargs
            )
            response = request.json()
        except Exception as e:
            self.flow = Flow(
                company=Active.namespace,
                period=Active.period,
                user=self.get_user(),
                handler='REST',
                endpoint=self.get_url(**kwargs),
                method=method,
                data=json.dumps(self.data, cls=DjangoJSONEncoder),
                request=json.dumps(self.get_data(**kwargs), cls=DjangoJSONEncoder),
                exception=str(e),
                error_code=1,
                prev_flow=self.prev_flow,
                took=(datetime.now()-start).total_seconds(),
                pid=self.pid,
                keyword1=self.keyword1,
                keyword2=self.keyword2,
                keyword3=self.keyword3
            )
            if self.skip_flow is False:
                self.flow.save()
            raise e
        else:
            internal_ref = None
            related_object = None
            if response and 'INTERNAL_REFERENCE' in response:
                internal_ref = response.get('INTERNAL_REFERENCE')
                if self.meta.RELATED_TABLE:
                    related_object=self.meta.RELATED_TABLE

            self.flow = Flow(
                company=Active.namespace,
                period=Active.period,
                user=self.get_user(),
                handler='REST',
                endpoint=self.get_url(**kwargs),
                method=method,
                data=json.dumps(self.data, cls=DjangoJSONEncoder),
                request=json.dumps(self.get_data(**kwargs), cls=DjangoJSONEncoder),
                prev_flow=self.prev_flow,
                response=json.dumps(response, cls=DjangoJSONEncoder),
                took=(datetime.now()-start).total_seconds(),
                pid=self.pid,
                success=True,
                related_object=related_object,
                internal_ref = internal_ref,
                keyword1=self.keyword1,
                keyword2=self.keyword2,
                keyword3=self.keyword3
            )
            if self.skip_flow is False:
                self.flow.save()
            return response

    def get_url(self, suffix=None, **kwargs):
        url = f'{Active.rest_url}{Active.rest_version}/{self.endpoint}'
        if suffix:
            url = f'{url}/{suffix}'
        return url

    def get_auth(self):
        from django.core.cache import cache
        firm = cache.get('active')
        return Auth(Token.get_or_create_token(self.user, firm=firm))

    def get_user(self):
        return Token.get_user(self.user)

    def request(self, method, *args, **kwargs):
        if hasattr(self, "endpoint") is False or self.endpoint is None:
            raise Exception('Endpoint tanımlanmamış!')
        
        params = None
        if 'params' in kwargs:
            params = kwargs.pop('params', None)
        
        return request(
            method,
            self.get_url(**kwargs),
            auth=self.get_auth(),
            json=self.get_data(**kwargs),
            params=params
        )

    def generate_xml_token(self):
        from hashlib import md5
        payload = f"{Active.xml_secret}*{self.pid}"
        return md5(payload.encode("utf-8")).hexdigest()

    def transfer_via_xml(self, item_name='', ignore_pid_check=None, **kwargs):
        if self.is_valid():
            self.set_xml(self.instance.to_xml(item_name=item_name))
            self.create_xml(ignore_pid_check=ignore_pid_check, **kwargs)

    def prepare_xml(self, item_name='', **kwargs):
        return self.instance.to_xml(item_name=item_name)

    def transfer_via_rest(self):
        if self.is_valid():
            self.set_data(self.instance.get_data())
            self.create()

    def update_via_xml(self, pk, item_name='', ignore_pid_check=None, **kwargs):
        if self.is_valid():
            self.set_xml(self.instance.to_xml(
                item_name=item_name,
                op='UPD',
                data_reference=pk
            ))
            self.create_xml(ignore_pid_check=ignore_pid_check, **kwargs)

    def send_to_edge(self, cmd, *args, **kwargs):
        if hasattr(self, "xml_endpoint") is False or self.xml_endpoint is None:
            raise Exception('Endpoint tanımlanmamış!')
        context = zmq.Context()
        socket = context.socket(zmq.REQ)
        socket.connect(Active.xml_server)
        socket.setsockopt(zmq.RCVTIMEO, settings.XML_CLIENT_TIMEOUT)        
        if 'ignore_pid_check' in kwargs and kwargs.get('ignore_pid_check'):
            cmd['ignore_pid_check'] = kwargs.get('ignore_pid_check')            
        socket.send_string(json.dumps(cmd, cls=DjangoJSONEncoder))
        response = json.loads(socket.recv_string())
        try:
            socket.close()
        except Exception as e:
            print(e)        
        return response
    
    def simple_object_update(self, logref, **kwargs):
        return self.update_via_object(self.xml_endpoint, {
            'ref': logref
        }, **kwargs)

    def update_via_object(self, do, data, **kwargs):
        """
        Usage note:
        # Use -> simple_object_update
        #
        sd = SalesOrderXML(partial=True, user=Active.default_rest_user)
        result = sd.update_via_object(
            sd.xml_endpoint,
            {
                'ref': logicalref
            },
            CANCELLED=1,
            X=Y
        )        
        """
        start = datetime.now()
        data.update({
            'op': 'UPDATE',
            'updates': kwargs
        })
        try:
            cmd = {
                'do': do,
                'pid': self.pid,
                'token': self.generate_xml_token(),
                'user': self.user,
                'data': data
            }
            response = self.send_to_edge(cmd)
        except Exception as e:
            self.flow = Flow(
                company=Active.namespace,
                period=Active.period,
                user=self.user,
                handler='XML',
                endpoint=Active.xml_server,
                method=do,
                data=json.dumps(kwargs, cls=DjangoJSONEncoder),
                request=json.dumps(cmd, cls=DjangoJSONEncoder),
                exception=str(e),
                error_code=1,
                prev_flow=self.prev_flow,
                took=(datetime.now()-start).total_seconds(),
                pid=self.pid,
                keyword1=self.keyword1,
                keyword2=self.keyword2,
                keyword3=self.keyword3
            )
            if self.skip_flow is False:
                self.flow.save()
        else:
            related_object = None
            internal_ref = None
            if self.meta and self.meta.RELATED_TABLE:
                if response['ok'] and response['response']:
                    if isinstance(response['response'], str):
                        resp = self.xml_2_dict(response['response'])
                    else:
                        resp = response['response']
                     
                    if "DATA_REFERENCE" in resp:
                        internal_ref = int(resp['DATA_REFERENCE'])
                        related_object = self.meta.RELATED_TABLE
                    if "INTERNAL_REFERENCE" in resp:
                        internal_ref = int(resp['INTERNAL_REFERENCE'])
                        related_object = self.meta.RELATED_TABLE
            self.flow = Flow(
                company=Active.namespace,
                period=Active.period,
                user=self.user,
                handler='XML',
                endpoint=Active.xml_server,
                method=do,
                data=json.dumps(kwargs, cls=DjangoJSONEncoder),
                request=json.dumps(cmd, cls=DjangoJSONEncoder),
                prev_flow=self.prev_flow,
                response=json.dumps(response, cls=DjangoJSONEncoder),
                took=(datetime.now()-start).total_seconds(),
                pid=self.pid,
                success=True,
                related_object=related_object,
                internal_ref=internal_ref,
                keyword1=self.keyword1,
                keyword2=self.keyword2,
                keyword3=self.keyword3
            )
            if self.skip_flow is False:
                self.flow.save()
            return response

    def xml_2_dict(self, xml):
        import xmltodict
        import re
        try:
            xml = re.sub(r"<\d+>", f'<{self.meta.XML_ROOT}>', xml)
            xml = re.sub(r"</\d+>", f'</{self.meta.XML_ROOT}>', xml)
            parsed = json.loads(json.dumps(xmltodict.parse(xml)))

            if self.meta.XML_ROOT in parsed:
                if self.meta.XML_SUBROOT in parsed[self.meta.XML_ROOT]:
                    clear = parsed[self.meta.XML_ROOT][self.meta.XML_SUBROOT]
                    if '@DBOP' in clear:
                        clear.pop('@DBOP')
                    return clear
        except Exception as e:
            print(e)
            logger.exception(e)
        return None   

    
    def read_xml_as_dict(self, logref):
        import xmltodict
        import re
        try:
            res = self.simple_read_xml(logref)
            if (res and 'ok' in res and \
                res['ok'] and 'response' in res and res['response']):
                resp = res['response']
                resp = re.sub(r"<\d+>", f'<{self.meta.XML_ROOT}>', resp)
                resp = re.sub(r"</\d+>", f'</{self.meta.XML_ROOT}>', resp)
                parsed = json.loads(json.dumps(xmltodict.parse(resp)))

                if self.meta.XML_ROOT in parsed:
                    if self.meta.XML_SUBROOT in parsed[self.meta.XML_ROOT]:
                        clear = parsed[self.meta.XML_ROOT][self.meta.XML_SUBROOT]
                        if '@DBOP' in clear:
                            clear.pop('@DBOP')
                        return clear
        except Exception as e:
            print(e)
            logger.exception(e)
        return None

    def simple_read_xml(self, logref):
        return self.read_xml(self.xml_endpoint, {
            'ref': logref
        })          
        
    def read_xml(self, do, data, **kwargs):
        """
        Usage note:
        # Use -> simple_object_update
        #
        """
        start = datetime.now()        
        data.update({
            'op': 'READ'
        })

        try:
            cmd = {
                'do': do,
                'pid': self.pid,
                'token': self.generate_xml_token(),
                'user': self.user,
                'data': data
            }
            response = self.send_to_edge(cmd)
        except Exception as e:
            self.flow = Flow(
                company=Active.namespace,
                period=Active.period,
                user=self.user,
                handler='XML',
                endpoint=Active.xml_server,
                method=self.xml_endpoint,
                data=json.dumps(kwargs, cls=DjangoJSONEncoder),
                request=json.dumps(cmd, cls=DjangoJSONEncoder),
                exception=str(e),
                error_code=1,
                prev_flow=self.prev_flow,
                took=(datetime.now()-start).total_seconds(),
                pid=self.pid,
                keyword1=self.keyword1,
                keyword2=self.keyword2,
                keyword3=self.keyword3
            )
            if self.skip_flow is False:
                self.flow.save()
        else:
            related_object = None
            internal_ref = None
            if self.meta and self.meta.RELATED_TABLE:
                if response['ok'] and response['response']:
                    resp = response['response']
                    if self.meta.XML_ROOT in resp and self.meta.XML_SUBROOT in resp[self.meta.XML_ROOT]:
                        if "DATA_REFERENCE" in resp[self.meta.XML_ROOT][self.meta.XML_SUBROOT]:
                            internal_ref = int(resp[self.meta.XML_ROOT][self.meta.XML_SUBROOT]['DATA_REFERENCE'])
                            related_object = self.meta.RELATED_TABLE
            self.flow = Flow(
                company=Active.namespace,
                period=Active.period,
                user=self.user,
                handler='XML',
                endpoint=Active.xml_server,
                method=self.xml_endpoint,
                data=json.dumps(self.data, cls=DjangoJSONEncoder),
                request=json.dumps(self.get_xml(), cls=DjangoJSONEncoder),
                prev_flow=self.prev_flow,
                response=json.dumps(response, cls=DjangoJSONEncoder),
                took=(datetime.now()-start).total_seconds(),
                pid=self.pid,
                success=True,
                related_object=related_object,
                internal_ref=internal_ref,
                keyword1=self.keyword1,
                keyword2=self.keyword2,
                keyword3=self.keyword3
            )
            if self.skip_flow is False:
                self.flow.save()
            return response
            
    def create_xml(self, *args, **kwargs):
        start = datetime.now()        
        try:
            cmd = {
                'do': self.xml_endpoint,
                'data': self.get_xml(),
                'pid': self.pid,
                'token': self.generate_xml_token(),
                'user': self.user
            }
            cmd.update(**kwargs)
            response = self.send_to_edge(cmd)
        except Exception as e:
            self.flow = Flow(
                company=Active.namespace,
                period=Active.period,
                user=self.user,
                handler='XML',
                endpoint=Active.xml_server,
                method=self.xml_endpoint,
                data=json.dumps(self.data, cls=DjangoJSONEncoder),
                request=json.dumps(self.get_xml(), cls=DjangoJSONEncoder),
                exception=str(e),
                error_code=1,
                prev_flow=self.prev_flow,
                took=(datetime.now()-start).total_seconds(),
                pid=self.pid,
                keyword1=self.keyword1,
                keyword2=self.keyword2,
                keyword3=self.keyword3
            )
            if self.skip_flow is False:
                self.flow.save()
            raise e
        else:
            related_object = None
            internal_ref = None
            if self.meta and self.meta.RELATED_TABLE:
                if response['ok'] and response['response']:
                    resp = response['response']
                    if self.meta.XML_ROOT in resp and self.meta.XML_SUBROOT in resp[self.meta.XML_ROOT]:
                        if "DATA_REFERENCE" in resp[self.meta.XML_ROOT][self.meta.XML_SUBROOT]:
                            internal_ref = int(resp[self.meta.XML_ROOT][self.meta.XML_SUBROOT]['DATA_REFERENCE'])
                            related_object = self.meta.RELATED_TABLE
            self.flow = Flow(
                company=Active.namespace,
                period=Active.period,
                user=self.user,
                handler='XML',
                endpoint=Active.xml_server,
                method=self.xml_endpoint,
                data=json.dumps(self.data, cls=DjangoJSONEncoder),
                request=json.dumps(self.get_xml(), cls=DjangoJSONEncoder),
                prev_flow=self.prev_flow,
                response=json.dumps(response, cls=DjangoJSONEncoder),
                took=(datetime.now()-start).total_seconds(),
                pid=self.pid,
                success=True,
                related_object=related_object,
                internal_ref=internal_ref,
                keyword1=self.keyword1,
                keyword2=self.keyword2,
                keyword3=self.keyword3
            )
            if self.skip_flow is False:
                self.flow.save()
            return response
