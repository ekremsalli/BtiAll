"""
 Tüm hakları BTI Bilişim Danışmanlık ve Yazılım Şirketi adına saklıdır.
 
"""

from django.conf import settings
import django.apps
import re
from django.core.cache import cache

class Active:
    name = 'default'
    data = settings.FIRMS['default']
    number = settings.FIRMS['default']['NR']
    namespace = settings.FIRMS['default']['NS']
    period = settings.FIRMS['default']['PER']
    prev_number = settings.FIRMS['default']['PREV_NR']
    prev_namespace = settings.FIRMS['default']['PREV_NS']
    prev_period = settings.FIRMS['default']['PREV_PER']
    rest_is_active = settings.FIRMS['default']['REST_IS_ACTIVE']
    rest_url = settings.FIRMS['default']['REST_URL']
    rest_head_key = settings.FIRMS['default']['REST_HEAD_KEY']
    rest_users = settings.FIRMS['default']['REST_USERS']
    rest_version = settings.FIRMS['default']['REST_VERSION']
    default_rest_user = settings.FIRMS['default']['DEFAULT_REST_USER']
    xml_server = settings.FIRMS['default']['XML_SERVER']
    xml_secret = settings.FIRMS['default']['XML_SECRET']
    xml_is_active = settings.FIRMS['default']['XML_IS_ACTIVE']
    settings = settings.FIRMS['default'].get('SETTINGS', {})


    @classmethod
    def load(cls, name, vars):
        cls.name = name
        cls.data = vars
        cls.number = vars['NR']
        cls.namespace = vars['NS']
        cls.period = vars['PER']
        cls.prev_number = vars['PREV_NR']
        cls.prev_namespace = vars['PREV_NS']
        cls.prev_period = vars['PREV_PER']
        cls.rest_is_active = vars['REST_IS_ACTIVE']
        cls.rest_url = vars['REST_URL']
        cls.rest_head_key = vars['REST_HEAD_KEY']
        cls.rest_users = vars['REST_USERS']
        cls.default_rest_user = vars['DEFAULT_REST_USER']
        cls.rest_version = vars['REST_VERSION']
        cls.xml_server = vars['XML_SERVER']
        cls.xml_secret = vars['XML_SECRET']
        cls.xml_is_active = vars['XML_IS_ACTIVE']
        cls.settings = vars.get('SETTINGS', {})

        reobj = re.compile(r"(LG?_)(\d{3})(_)(\d{2})?(.+)")

        # change every model meta field
        if django.apps.apps.models_ready:
            for model in django.apps.apps.get_models():
                if "erp.model" in str(model):
                    check = reobj.search(model._meta.db_table)
                    if check:
                        grps = check.groups()
                        if grps[3]:
                            model._meta.db_table = f'{grps[0]}{cls.namespace}_{cls.period}{grps[4]}'
                        else:
                            model._meta.db_table = f'{grps[0]}{cls.namespace}_{grps[4]}'
    @classmethod
    def load_firm(cls, name):
        if name in settings.FIRMS:
            cls.load(name, settings.FIRMS[name])

    @classmethod
    def load_defaults(cls):
        cls.load('default', settings.FIRMS['default'])

    @classmethod
    def load_firm_via_nr(cls, nr):
        items = {v['NR']: k for k,v in settings.FIRMS.items()}
        if nr in items:
            cls.load_firm(items[nr])
            cache.set('active', items[nr])

    @classmethod
    def clear_cache(cls):
        cache.delete('active')



Active = Active()
