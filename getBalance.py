from main import API_SECRET, API_ENDPOINT, API_KEY, _getSignature, _getCurrentTime
import requests, argparse

def onGetBalance(symbol, recvWindow, timestamp):
    param = 'symbol=%s&recvWindow=%s&timestamp=%s' % (symbol, recvWindow, timestamp) 
    signature = _getSignature(param, API_SECRET)
    param += "&signature=" + signature

    res = requests.get(API_ENDPOINT + '/v1/account?' + param, data = {}, headers={
        'Content-Type': 'application/json',
        'X-MBX-APIKEY': API_KEY
    }).json()
    return res['availableBalance']

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument("-s", "--symbol", help="Input symbol", required=True)
    parser.add_argument('-w', '--recvWindow', help="Processing milliseconds after timestamp. Default=5000", default=5000)

    args = parser.parse_args()

    res = onGetBalance(args.symbol, args.recvWindow, _getCurrentTime())
    print(res)