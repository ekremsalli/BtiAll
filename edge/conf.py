SECRET = "Frux8GruejO"
BINDS = ["tcp://*:5555"]

HISTORY_TRACK = 5000

DEBUG = 1

USERS = [
    {
        'username': 'BTI',
        'pwd': '3333',
        'active': True,
        'company': 20,
        'period': 1
    },
    {
        'username': 'RobotPOS',
        'pwd': '1234',
        'active': True,
        'company': 20,
        'period': 1
    },
    {
        'username': 'DepoX',
        'pwd': '1234',
        'active': True,
        'company': 20,
        'period': 1
    },
    {
        'username': 'AKTARIM',
        'pwd': '1234',
        'active': True,
        'company': 20,
        'period': 1
    },
    {
        'username': 'Eba_',
        'pwd': '1234',
        'active': True,
        'company': 20,
        'period': 1
    }
]

try:
    from local_conf import *
except ImportError:
    pass
except Exception as e:
    print(e)
