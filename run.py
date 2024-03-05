# example_program.py

import sys
import json
import time
import json
import traceback
from ib_insync import *
import subprocess



def place_order():
    global position_opened

    try:
        if len(sys.argv) != 2:
            print("Usage: python example_program.py args_json")
            return

        args_json = sys.argv[1]
        data = json.loads(args_json)
        print(data)
        # return data
        ib = IB()
        ib.connect("127.0.0.1", 7496, clientId=1)
        time.sleep(1)
        contract="NA"
        if data['contract']=="FUTURE":
            contract=Future(symbol=data['symbol'],lastTradeDateOrContractMonth=data['expiry'],exchange=data['exchange'])
        if data['contract']=="STOCK":
            contract=Stock(data['symbol'],data['exchange'],"USD")

        order = MarketOrder(data['side'].upper(), int(data['quantity']))
        trade=ib.placeOrder(contract,order)
        ib.disconnect()  
        return {"hello":str(trade)}

    except Exception:
        return str(traceback.format_exc())

if __name__ == "__main__":
    place_order()
