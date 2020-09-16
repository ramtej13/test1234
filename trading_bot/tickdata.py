from kiteconnect import KiteConnect
from kiteconnect import KiteTicker
import websocket
import time
import json
import random


api_key = 'hdtlbz2j74tym170'
api_secret = 'cdh6zl7tjiokssi1acwt46nft3z6nxx1'
access_token = '526e2FolYJtiVt8GvvF63m2LhurSAKmQ'

kite = KiteConnect(api_key=api_key)
kite.set_access_token(access_token)
kws = KiteTicker(api_key,access_token)


wsw = websocket.WebSocket()
wsw.connect('ws://localhost:8000/ws/trading_bot/stock_data/')

inst_token = [5633,6401,3861249,4451329,25601,325121,40193,41729,49409,
               54273,60417,70401,1510401,4267265,4268801,81153,85761,1195009,
              1214721,94977,98049,103425,108033,2714625,112129,2911489,558337,
              558337,134657,140033,1790465,2029825,2763265,320001,160001,160769,
              175361,177665,5215745,3876097,1215745,486657,197633,215553,2800641,
              3721473,3771393,225537,232961,1256193,4314113,245249,173057,261889,
              1207553,1895937,3463169,2585345,315393,2513665,1850625,340481,341249,
              345089,2747905,348929,359937,356865,364545,7712001,1270529,4774913,
              377857,3677697,2863105,2883073,2865921,1346049,7458561,408065,415745,
              424961,1723649,3001089,4632577,7670273,462849,492033,6386689,511233,
              2939649,2672641,519937,3400961,4879617,1041153,2815745,2674433,7982337,
              548353,4488705,3675137,1076225,582913,6054401,1629185,8042241,593665,
              4598529,2955009,3924993,2977281,2748929,136475140,633601,3689729,617473,
              2905857,3660545,681985,2730497,3834113,3365633,523009,731905,4708097,3930881,
              737793,738561,141569,758529,779521,794369,806401,837889,1102337,1887745,
              857857,3431425,871681,873217,878593,884737,4343041,877057,895745,2953217,
              3465729,897537,900609,3529217,2170625,4278529,4369665,2952193,2752769,
              2889473,784129,951809,969473,3050241,975873]

def tickkkkk():
    def on_ticks(ws, ticks):
        b = {0:{'instrument_token': 5633, 'last_price': 168, 'volume': 898174,'change': -0.42674253200568585 ,'ohlc': {'open': 35.1, 'high': 35.25, 'low': 34.9, 'close': 35.15}}}

        for i in range(len(inst_token)):
            b[i] = {'instrument_token': inst_token[i], 'last_price': 168, 'volume': 0,'change': 0 ,'ohlc': {'open': 0, 'high': 0, 'low': 0, 'close': 0}}

        for ticks in ticks:
            for i in range(len(inst_token)):
                if ticks['instrument_token'] == inst_token[i]:
                    b[i]['last_price'] = ticks['last_price']
                    b[i]['volume'] = ticks['volume']
                    b[i]['change'] = ticks['change']
                    b[i]['ohlc']['open'] = ticks['ohlc']['open']
                    b[i]['ohlc']['high'] = ticks['ohlc']['high']
                    b[i]['ohlc']['low'] = ticks['ohlc']['low']
                    b[i]['ohlc']['close'] = ticks['ohlc']['close']
                # elif ticks['instrument_token'] == 6401:
                #     b[1]['last_price'] = ticks['last_price']
                # elif ticks['instrument_token'] == 3861249:
                #     b[2]['last_price'] = ticks['last_price']
                # elif ticks['instrument_token'] == 4451329:
                #     b[3]['last_price'] = ticks['last_price']
                # print(random.randint(1,100),ticks['last_price'])
        wsw.send(json.dumps(b))

        # print(b)


        #     a['command'] = 'new_message'
        #     a['message'] = a['last_quantity']
        #     a['from'] = 'hello'
        #     b.append(a)

        # wsw.send(json.dumps(ticks))
        # print(random.randint(1,100),ticks)
        # print(len(b))

        # if len(ticks) == 4:
        #     wsw.send(json.dumps(ticks))
        #     print("helllo")

        # print(tickss for tickss in ticks)
        # print(len(b))

    def on_connect(ws, response):
        ws.subscribe(inst_token)
        ws.set_mode(ws.MODE_QUOTE, inst_token)
        print("o")

    # def on_connect(ws, response):
    #     ws.subscribe(inst_token)
    #     print("connected")

    kws.on_ticks = on_ticks
    kws.on_connect = on_connect
    kws.connect()

tickkkkk()