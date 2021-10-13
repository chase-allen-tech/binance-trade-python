####################################################################################
#  Trade with Binance API
####################################################################################

import requests, hmac, hashlib, json
from datetime import datetime

API_KEY = "d128ad3126390ed8b40ae6f839b24492d4ce6d5a4d4dfdf2d52d374b3c4d61bb"
API_SECRET = "a63a26280782019d00356226af8ee783aa97a5cf43e343229939a72f2b15bc80"
API_ENDPOINT = "https://testnet.binancefuture.com/fapi"

####################################################################################

def _getCurrentTime():
    try:
        res = requests.get(API_ENDPOINT + '/v1/time').json()
        readable = datetime.fromtimestamp(res['serverTime'] / 1e3)
        print('[Server Time]', readable)
        return res['serverTime']
    except:
        print("[Server Time Error]")
        return None

def _getCurrentPrice(symbol):
    res = requests.get(API_ENDPOINT + '/v1/ticker/price?symbol=' + symbol).json()
    _printJson(res)
    return res['price']

def _getSignature(query, key):
    key = bytes(key, 'UTF-8')
    query = query.encode()
    h = hmac.new(key, query, hashlib.sha256)
    return h.hexdigest()

def _printJson(data):
    print(json.dumps(data, indent=2))

if __name__ == '__main__':
    print("Execute commands in each files.")