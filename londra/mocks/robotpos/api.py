from os import path
import json

from flask import Flask, request


app = Flask(__name__)
itypes = {
    '3': 'sales',
    '1': 'rev'
}

@app.route('/ingiltere/api/Data', methods=['POST'])
def get_data():
    data = request.form
    itype = data.get('Type')
    start = data.get('StartDate').split()[0]
    branch = data.get('BranchCode')

    if itype not in itypes:
        return {
            'Status': False,
            'Message': 'Unknown type!'
        }

    name = f'ing_{itypes[itype]}_{start}_{branch}.json'
    full_path = f'mocks/robotpos/data/{name}'
    print(full_path)
    if path.exists(full_path):
        with open(full_path, 'r') as fp:
            return {
                'Status': True,
                'Data': json.loads(fp.read())
            }
    else:
        return {
            'Status': False,
            'Message': 'Unknown file!'
        }

app.run(debug=True)
