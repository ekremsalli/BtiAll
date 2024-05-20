import csv
import io
from datetime import datetime
from rest_framework.views import APIView
from common.views import Bti
from rest_framework.response import Response
from django.conf import settings
import pysftp

from app.models.other import Payrolls
from app.models.employee import Employees
from app.serializers.payroll import PayrollSerializer


class PayrollView(Bti, APIView):
    def put(self, request):
        try:
            s = io.StringIO()
            csv.writer(s).writerows(request.data)
            s.seek(0)
            now = datetime.today()
            name = f'VALEO_BTI_{str(now.day).zfill(2)}_{str(now.month).zfill(2)}_{now.year}_{str(now.hour).zfill(2)}_{str(now.minute).zfill(2)}.csv'
            sett = settings.FTP.get('VALEO')
            cnopts = pysftp.CnOpts()
            cnopts.hostkeys = None
            with pysftp.Connection(
                    sett.get('Host'),
                    username=sett.get('Username'),
                    password=sett.get('Password'),
                    cnopts=cnopts) as sftp:
                with sftp.cd(sett.get('Path')):
                    sftp.putfo(s, name)
        except Exception as e:
            return Response({
                'success': False,
                'message': str(e)
            })
        else:
            return Response({
                'success': True,
                'name': name
            })

    def post(self, request, *args, **kwargs):
        serializer = PayrollSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        start = datetime.strptime(serializer.data.get('start'), '%Y/%m/%d')
        end = datetime.strptime(serializer.data.get('end'), '%Y/%m/%d')

        employees = []
        firm = []

        firmx = serializer.data.get('firm')
        if firmx:
            firm = firmx
        else:
            firm = None
        collar_type = None
        worker_type = serializer.data.get('worker_type')
        if worker_type == 1:
            collar_type = 'B'
        elif worker_type == 2:
            collar_type = 'M'
        empx = serializer.data.get('employees')
        if empx:
            employees = empx
        else:
            employees = None
        employees = Payrolls.prepare(
            serializer.data.get('db'),
            start,
            end,
            employees=employees,
            collar_type=collar_type,
            firm=firm
        )
        config = settings.GECO_MAPPING[serializer.data.get('db')]['DATASSIST']
        for employee in employees:
            data = []
            for line in employee.get('geco'):
                convert = Payrolls.reduce(line, config)
                temp = {
                    'BaslaTarihi': line.get('BaslaTarihi'),
                    'BitisTarihi': line.get('BitisTarihi')
                }
                temp.update(convert)
                data.append(temp)
            employee['daily'] = data
            employee['monthly'] = Payrolls.montly(employee.get('geco'), config)

        return Response({
            'start': start,
            'end': end,
            'employees': employees
        })
