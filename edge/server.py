import asyncio as ai
from datetime import datetime
import json
import sys
import signal
import traceback


import zmq
import xmltodict

import conf

if sys.platform == 'win32':
    ai.set_event_loop_policy(ai.WindowsSelectorEventLoopPolicy())
    from load import unity
else:
    raise Exception('Platform supports only win32 sys.')

import zmq.asyncio

apps = {}
q = ai.Queue()

object_map = {
    'doMaterialSlip': 'MATERIAL_SLIPS',
    'doOverheadPoolAcc': 'OHP_ACCOUNTS',
    'doGLVoucher': 'GL_VOUCHERS',
    'doBankAccount': 'BANK_ACCOUNTS',
    'doBank': 'BANKS',
    'doBankVoucher': 'BANK_VOUCHERS',
    'doSlCampaign': 'SALES_CAMPAIGNS',
    'doPrCampaign': 'PURCHASE_CAMPAIGNS',
    'doSafeDeposit': 'SAFE_DEPOSITS',
    'doSafeDepositTrans': 'SD_TRANSACTIONS',
    'doCQPnRoll': 'CQPN_ROLLS',
    'doTransCqPn': 'CQPN_TRANSFERS',
    'doAccountsRP': 'AR_APS',
    'doARAPVoucher': 'ARP_VOUCHERS',
    'doArpShipLic': 'ARP_SHIPMENT_LOCATIONS',
    'doSalesDisc': 'SALES_DISCOUNTS',
    'doPurchDisc': 'PURCHASE_DISCOUNTS',
    'doSalesDispatch': 'SALES_DISPATCHES',
    'doPurchDispatch': 'PURCHASE_DISPATCHES',
    'doCountry': 'COUNTRIES',
    'doCity': 'CITIES',
    'doDistrict': 'DISTRICTS',
    'doTown': 'TOWNS',
    'doPostCode': 'POST_CODES',
    'doSalesInvoice': 'SALES_INVOICES',
    'doPurchInvoice': 'PURCHASE_INVOICES',
    'doPurchOrderSlip': 'PURCHASE_ORDERS',
    'doSalesOrderSlip': 'SALES_ORDERS',
    'doDistOrder': 'DIST_ORDERS',
    'doPurchProm': 'PURCHASE_PROMOTIONS',
    'doSalesProm': 'SALES_PROMOTIONS',
    'doSalesService': 'SALES_SERVICES',
    'doPurchService': 'PURCHASE_SERVICES',
    'doCypCodes': 'CYP_CODES',
    'doSpeCodes': 'SPE_CODES',
    'doPPGCodes': 'PPG_CODES',
    'doDistVehicle': 'VECHILES',
    'doDistRouting': 'DIST_ROUTINGS',
    'doPayPlan': 'PAYMENT_PLANS',
    'doSalesExpn': 'SALES_EXPENSES',
    'doPurchExpn': 'PURCHASE_EXPENSES',
    'doSalesPriceItem': 'ITEM_SALES_PRICE',
    'doPurchPriceItem': 'ITEM_PURCHASE_PRICE',
    'doSlsRoute': 'CST_SALES_ROUTES',
    'doSlsTarget': 'CST_SALES_TARGET',
    'doSalesmanCl': 'CLSALESMANS',
    'doSalesPriceService': 'SERVICE_SALES_PRICE',
    'doPurchPriceService': 'SERVICE_PURCHASE_PRICE',
    'doStdCostPrd': 'STD_COST_PERIOD',
    'doMaterial': 'ITEMS',
    'doItemAlters': 'ITEM_ALTERNATES',
    'doItemBOM': 'ITEM_BOM_ASGN',
    'doItmStdCosts': 'STD_ITM_COSTS',
    'doStdBOMCosts': 'STD_BOM_COSTS',
    'doFARegistry': 'FIXED_ASSET_REGISTRY',
    'doSerialLot': 'SERIAL_LOT_RECORDS',
    'doUnitSet': 'UNIT_SETS',
    'doItemClsAsgn': 'M_M_Class_Tree',
    'doItChCodes': 'ITEM_CHARACTERISTICS',
    'doGrpCodes': 'GRP_CODES',
    'doLocCodes': 'LOC_CODES',
    'doDelCodes': 'DEL_CODES',
    'doQCCSet': 'QCCSETS',
    'doWstChars': 'characteristics',
    'doWorkStat': 'WORKSTATS',
    'doWStdCosts': 'doWStdCosts',
    'doWstGroup': 'WSTGROUPS',
    'doEmployee': 'EMPLOYEES',
    'doEmplCost': 'EMPLCOSTS',
    'doEmpGroup': 'EMPGROUPS',
    'doWrStCost': 'WRSTCOSTS',
    'doShifts': 'SHIFTS',
    'doShiftAsg': 'SHIFTASG',
    'doOperation': 'OPERATIONS',
    'doRouting': 'ROUTINGS',
    'doBOM': 'BOMS',
    'doPrdParams': 'PRODPARAMS',
    'doGLAccount': 'GL_ACCOUNTS'
}

def signal_handler(signal, frame):
    global apps
    print('\nbye bye')
    for app in apps.keys():
        try:
            apps[app].Logout()
        except:
            pass
    del apps
    sys.exit(0)

def setup():
    global apps

    for user in conf.USERS:
        if 'username' in user and 'pwd' in user and 'company' in user:
            username = user.get('username')
            pwd = user.get('pwd')
            company = user.get('company')
            if 'active' in user and user['active']:
                if username not in apps:
                    apps[username] = unity.UnityApplication()
                    apps[username].Login(
                        username,
                        pwd,
                        company,
                        user.get('period', None)
                    )

                
async def worker():
    while True:
        try:
            raw, socket = await q.get()
            what = raw['do']
            #print('raw', raw)
            if what in object_map.keys():
                if 'data' in raw and raw['data'] and isinstance(raw['data'], dict):
                    if raw['data']['op'] == 'READ':
                        await doRead(raw, socket, getattr(unity.constants, what), raw['data']['ref'])
                    elif raw['data']['op'] == 'UPDATE':
                        await doUpdateViaObject(raw, socket, getattr(unity.constants, what), raw['data']['ref'], raw['data']['updates'])
                    elif raw['data']['op'] == 'DELETE':
                        await doDelete(raw, socket, getattr(unity.constants, what), raw['data']['ref'])
                else:
                    await doRecord(raw, socket, object_map[what], getattr(unity.constants, what))
            elif what == 'CancelInvoice':
                await CancelInvoice(raw, socket)
            elif what == 'MaterialTransactionTransfer':
                await MaterialTransactionTransfer(raw, socket)
            elif what == 'OrderShipping':
                await OrderShipping(raw, socket)
            elif what == 'ShredDispatch':
                await ShredDispatch(raw, socket)
            elif what == 'SetDistOrderStatus':
                pass
                #await SetDistOrderStatus(raw, socket)
            elif what == 'OrderBilling':
                await OrderBilling(raw, socket)
            elif what == 'DebtClose':
                await DebtClose(raw, socket)
            elif what == 'DispatchBilling':
                await DispatchBilling(raw, socket)
            elif what == 'ImportImage':
                await ImportImage(raw, socket)
            elif what == 'Count':
                await Count(raw, socket)
            elif what == 'Time':
                await send_message(socket, {
                    'ok': True,
                    'Time': str(datetime.now())
                })
            elif what == 'Ping':
                await send_message(socket, {
                    'ok': True,
                    'desc': 'Pong!'
                })
            else:
                await send_message(socket, {
                    'ok': False,
                    'desc': 'Unknown call: %s'.format(raw['do']),
                    'code': 1005
                })

            q.task_done()
        except Exception as e:
            print(e)
            traceback.print_exc()
        await ai.sleep(.01)


async def doDelete(raw, socket, dobject, ref):
    global apps
    try:
        record = apps[raw['user']].NewDataObject(dobject)
        if record.Delete(ref):
            await send_message(socket, {
                'ok': True,
                'response': f'{ref} successfully deleted!',
            })                
        else:
            await send_message(socket, {
                'ok': False,
                'desc': 'Data not deleted',
                'code': 5001
            })
    except Exception as e:
        print(e)
        traceback.print_exc()
            
async def doRead(raw, socket, dobject, ref):
    global apps
    try:
        record = apps[raw['user']].NewDataObject(dobject)
        ok = record.Read(ref)
        if ok:
            ok, xml = record.ExportToXmlStr(dobject)
            if ok:
                await send_message(socket, {
                    'ok': ok,
                    'response': xml,
                })                
            else:
                await send_message(socket, {
                    'ok': False,
                    'desc': 'Data not found',
                    'code': 4000
                })                
        else:
            await send_message(socket, {
                'ok': False,
                'desc': 'Data not found',
                'code': 4001
            })       
    except Exception as e:
        print(e)
        traceback.print_exc()
    
async def doUpdateViaObject(raw, socket, dobject, ref, updates):
    global apps
    try:
        record = apps[raw['user']].NewDataObject(dobject)
        ok = record.Read(ref)
        if ok:
            for key, value in updates.items():
                record.DataFields.FieldByName(key).Value = value


            if record.Post() is False:
                if record.ErrorCode != 0:
                    print(apps[raw['user']].GetLastError(), apps[raw['user']].GetLastErrorString())
                    await send_message(socket, {
                        'ok': False,
                        'desc': str(record.DBErrorDesc) if str(record.DBErrorDesc) else apps[raw['user']].GetLastErrorString(),
                        'code': 1007
                    })
                else:
                    await send_message(socket, {
                        'ok': False,
                        'desc': ", ".join([record.ValidateErrors(i).Error for i in range(record.ValidateErrors.Count)]),
                        'code': 1007
                    })
            else:
                ok, xml = record.ExportToXmlStr(dobject)
                if ok:
                    await send_message(socket, {
                        'ok': ok,
                        'response': xml
                    })
                else:
                    await send_message(socket, {
                        'ok': ok,
                        'response': xml
                    })
        else:
            await send_message(socket, {
                'ok': False,
                'desc': 'Data not found for update',
                'code': 4002
            })       
    except Exception as e:
        print(e)
        traceback.print_exc()
        raise e
    
async def doRecord(raw, socket, doing, dobject):
    global apps
    try:
        data = apps[raw['user']].NewDataObject(dobject)
        ok = data.ImportFromXmlStr(doing, raw['data'])
        if ok:
            try:
                if 'fill_acc_codes' in raw and raw['fill_acc_codes']:
                    data.FillAccCodes()
            except Exception as e:
                print(e)
                traceback.print_exc()
                return
            
            if data.Post() is False:
                if data.ErrorCode != 0:
                    print(apps[raw['user']].GetLastError(), apps[raw['user']].GetLastErrorString())
                    await send_message(socket, {
                        'ok': False,
                        'desc': str(data.DBErrorDesc) if str(data.DBErrorDesc) else apps[raw['user']].GetLastErrorString(),
                        'code': 1007
                    })
                else:
                    await send_message(socket, {
                        'ok': False,
                        'desc': ", ".join([data.ValidateErrors(i).Error for i in range(data.ValidateErrors.Count)]),
                        'code': 1007
                    })
            else:
                ok, xml = data.ExportToXmlStr(doing)
                if ok:
                    response = xmltodict.parse(xml)
                    await send_message(socket, {
                        'ok': ok,
                        'response': response
                    })
                else:
                    await send_message(socket, {
                        'ok': ok,
                        'response': xml
                    })

        else:
            await send_message(socket, {
                'ok': False,
                'desc': 'Not valid xml',
                'code': 1006
            })
    except:
        traceback.print_exc()
    finally:
        try:
            del data
        except:
            pass

async def CancelInvoice(raw, socket):
    global apps
    try:
        if "ref" not in raw['data'] or raw['data']['ref'] is None:
            await send_message(socket, {
                'ok': False,
                'desc': 'Invoice logicalref is mandatory field.',
                'code': 2003
            })
        else:
            ok = apps[raw['user']].CancelInvoice(raw['data']['ref'])
            if ok:
                await send_message(socket, {
                    'ok': True,
                    'ref': raw['data']['ref']
                })
            else:
                await send_message(socket, {
                    'ok': False,
                    'desc': apps[raw['user']].GetLastErrorString(),
                    'code': 2001
                })
    except Exception as e:
        traceback.print_exc()
        await send_message(socket, {
            'ok': False,
            'desc': str(e),
            'code': 2002
        })

async def MaterialTransactionTransfer(raw, socket):
    global apps
    try:
        data = raw['data']
        if "old" in data and "new" in data and "period" in data:
            ok = apps[raw['user']].MaterialTransactionTransfer(data['old'], data['new'], data['period'])
            if ok:
                await send_message(socket, {
                    'ok': True,
                    'new': data['new']
                })
            else:
                await send_message(socket, {
                    'ok': False,
                    'desc': apps[raw['user']].GetLastErrorString(),
                    'code': 3003
                })
        else:
            await send_message(socket, {
                'ok': False,
                'desc': 'old, new and period is mantatory fields.',
                'code': 3001
            })
    except Exception as e:
        traceback.print_exc()
        await send_message(socket, {
            'ok': False,
            'desc': str(e),
            'code': 3002
        })


async def Count(raw, socket):
    data = raw['data']
    await send_message(socket, {
        'ok': True,
        'count': len(data)
    })

async def ImportImage(raw, socket):
    global apps
    try:
        data = raw['data']
        ok = apps[raw['user']].ImportBase64EncodedImage(
            data['doctype'],
            data['logref'],
            data['itype'],
            data['index'],
            data['image']
        )
        if ok:
            await send_message(socket, {
                'ok': True
            })
        else:
            await send_message(socket, {
                'ok': False,
                'desc': apps[raw['user']].GetLastErrorString(),
                'code': 4003
            })
    except Exception as e:
        traceback.print_exc()
        await send_message(socket, {
            'ok': False,
            'desc': str(e),
            'code': 4002
        })

async def _not_imp(raw, socket):
    await send_message(socket, {
        'ok': False,
        'desc': 'Not implemented.',
        'code': 999
    })

async def OrderShipping(raw, socket):
    await _not_imp(raw, socket)

async def ShredDispatch(raw, socket):
    await _not_imp(raw, socket)

async def OrderBilling(raw, socket):
    await _not_imp(raw, socket)

async def DispatchBilling(raw, socket):
    await _not_imp(raw, socket)

async def DebtClose(raw, socket):
    await _not_imp(raw, socket)

async def run(bind):
    tracking = set()
    ctx = zmq.asyncio.Context()
    socket = ctx.socket(zmq.REP)
    socket.bind(bind)
    print(f'{bind} is active!')
    while True:
        try:
            message = await socket.recv()
            if conf.DEBUG:
                print("Received request:", message)
            try:
                raw = json.loads(message.decode("utf-8"))
            except:
                await send_message(socket, {
                    'ok': False,
                    'desc': 'Bad packet',
                    'code': 1000
                })
            # validate base requirements and put to q
            else:
                kcheck = ["do", "data", "pid", "token", "user"]
                param_check = [kc in raw and raw.get(kc) for kc in kcheck]
                if all(param_check):
                    user = raw.get('user')
                    pid = raw.get('pid')
                    do = raw.get('do')
                    token = raw.get('token')
                    error = False
                    if token != generate_xml_token(pid):
                        await send_message(socket, {
                            'ok': False,
                            'desc': 'Invalid token',
                            'code': 1003
                        })
                        error = True

                    if "ignore_pid_check" not in raw and pid in tracking:
                        await send_message(socket, {
                            'ok': False,
                            'desc': 'Processed before',
                            'code': 1002
                        })
                        error = True
                    if user not in apps.keys():
                        await send_message(socket, {
                            'ok': False,
                            'desc': 'Unknown user',
                            'code': 1001
                        })
                        error = True


                    if error is False:
                        if pid not in tracking:
                            tracking.add(pid)
                            if len(tracking) > conf.HISTORY_TRACK:
                                tracking.pop()

                        await q.put((raw, socket))

                else:
                    await send_message(socket, {
                        'ok': False,
                        'desc': 'Missing required params',
                        'code': 1004
                    })

        except Exception as e:
            print(e)
            traceback.print_exc()
        finally:
            await ai.sleep(0.01)

def generate_xml_token(pid):
    from hashlib import md5
    payload = f"{conf.SECRET}*{pid}"
    return md5(payload.encode("utf-8")).hexdigest()


async def send_message(socket, data):
    await socket.send_string(json.dumps(data), zmq.NOBLOCK)

async def control():
    while True:
        await ai.sleep(.5)

async def main(bind):
    futures = [control(), run(bind), worker()]
    await ai.gather(*futures, return_exceptions=True)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise Exception('run.py tcp://*:3336')
    signal.signal(signal.SIGINT, signal_handler)
    setup()
    try:
        loop = ai.get_event_loop()
        loop.run_until_complete(main(sys.argv[1]))
    except KeyboardInterrupt:
        print("got keyboard interrupt")
        loop.close()
        sys.exit()
