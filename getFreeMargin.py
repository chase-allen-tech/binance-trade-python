from datetime import time
import requests, argparse

from main import API_SECRET, API_ENDPOINT, API_KEY, _getSignature, _getCurrentTime, _printJson

def onGetMargin(recvWindow, timestamp):

    param = 'recvWindow=%s&timestamp=%s' % (recvWindow, timestamp) 
    signature = _getSignature(param, API_SECRET)
    param += "&signature=" + signature
    try:
        res = requests.get(API_ENDPOINT + '/v2/account?' + param, data = {}, headers={
            'Content-Type': 'application/json',
            'X-MBX-APIKEY': API_KEY
        }).json()
        freeMargin = float(res['totalWalletBalance']) - float(res['totalMarginBalance'])
        return freeMargin
    except Exception as e:
        return None

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('-w', '--recvWindow', help="Processing milliseconds after timestamp. Default=5000", default=5000)

    args = parser.parse_args()

    margin = onGetMargin(args.recvWindow, _getCurrentTime())
    print('[Free Margin]', margin)
    