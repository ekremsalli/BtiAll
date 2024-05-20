import csv
import json
from django.core.serializers.json import DjangoJSONEncoder


from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.db import IntegrityError

from app_v1.serializers.service import RequestSerializer
from app_v1.models import OpQue

class Command(BaseCommand):
    help = "Read from csv file"

    def add_arguments(self , parser):
        parser.add_argument('file', type=str, 
            help='CSV file')
        parser.add_argument(
            'delimiter', 
            help='delimiter', 
            type=str, 
            default=';',
            nargs='?'
        )

    def handle(self, *a, **kw):
        try:
            with open(kw.get('file'), 'r') as fp:
                reader = list(
                    csv.reader(
                        fp, 
                        delimiter=kw.get('delimiter')
                    )
                )
                lines = []
                if reader:
                    header = reader[0]
                    for row in reader[1:]:
                        lines.append(dict(zip(header, row)))
                
                data = {
                    'lines': lines
                }
                req = RequestSerializer(data=data)
                req.is_valid(raise_exception=True)
                data = req.data
                for line in data.get('lines'):
                    try:
                        OpQue.objects.create(
                            day=line.get('day'),
                            identifier=line.get('pid'),
                            op_code=line.get('op_code'),
                            commission_amount=line.get('commission_amount'),
                            data=json.dumps(line, cls=DjangoJSONEncoder)
                        )
                    except IntegrityError as e:
                        print(line.get('pid'), e)
        except Exception as e:
            raise CommandError(e)
