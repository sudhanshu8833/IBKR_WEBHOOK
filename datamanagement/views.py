import logging
from django.http import HttpResponse,JsonResponse

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
import traceback
from ib_insync import *

# Create your views here.
from django.contrib import messages
import threading
import random
import string
from .models import *
import time
from datetime import datetime, date


errors=[]
logger = logging.getLogger('dev_log')

# ib = IB()
# ib.connect("127.0.0.1", 7496, clientId=1)

def place_order(data):
    global position_opened

    try:
        contract="NA"
        if data['contract']=="FUTURE":
            contract=Future(symbol=data['symbol'],lastTradeDateOrContractMonth=data['expiry'],exchange=data['exchange'])
        if data['contract']=="STOCK":
            contract=Stock(data['symbol'],data['exchange'],"USD")
        order = MarketOrder(data['side'].upper(), int(data['quantity']))
        trade=ib.placeOrder(contract,order)
        return trade
    except Exception:

        logger.info(str(traceback.format_exc()))
        return str(traceback.format_exc())

        



@csrf_exempt
def tradingview_webhook(request):
    try:

        '''
        {   "symbol":"ES",
            "side":"BUY",
            "price":"120",
            "contract":"FUTURE",
            "exchange":"CME",
            "expiry":"20241220",
            "passphrase":"dfkhskhfiuaehg",
            "quantity":"1"
        }
        '''

        data = json.loads(request.body.decode("utf-8"))
        logger.info(str(data))

        if request.method == "POST":        
            admin=Admin.objects.all()[0]
            passphrase=data['passphrase']
            pp = str(passphrase)
            data['Order_id']=[]

            if pp== admin.paraphrase:
                stock=data['symbol']
                price=data['price']

                record=positions(symbol=stock,time=datetime.now(),price=price,order_type=data['order_type'])
                record.save()

                # if(admin.status==True):
                try:
                    id=place_order(data)
                    data['Order_id'].append(id)
                    logger.info(data)
                except Exception:
                    logger.info(str(traceback.format_exc()))
                return JsonResponse(data)

            else:
                return JsonResponse({"error":"passphrase is wrong"})

        return JsonResponse({"error":"send a valid post request"})
        
    except Exception:

        logger.info(str(traceback.format_exc()))
        errors.append(str(traceback.format_exc()))
        return JsonResponse({"error":str(traceback.format_exc())})


