import requests, argparse

from getBalance import onGetBalance
from main import API_SECRET, API_ENDPOINT, API_KEY, _getSignature, _getCurrentTime, _printJson

def onGetProfit(symbol, recvWindow, timestamp):
    param = 'symbol=%s&recvWindow=%s&timestamp=%s' % (symbol, recvWindow, timestamp) 
    signature = _getSignature(param, API_SECRET)
    param += "&signature=" + signature

    res = requests.get(API_ENDPOINT + '/v2/positionRisk?' + param, data = {}, headers={
        'Content-Type': 'application/json',
        'X-MBX-APIKEY': API_KEY
    }).json()
    return res[0]['unRealizedProfit'], res[0]

def onGetEquity(symbol, recvWindow):
    currTime = _getCurrentTime()
    balance = onGetBalance(symbol, recvWindow, currTime)
    profit, _ = onGetProfit(symbol, recvWindow, currTime)
    equity = float(balance) + float(profit)
    return equity

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument("-s", "--symbol", help="Input symbol", required=True)
    parser.add_argument('-w', '--recvWindow', help="Processing milliseconds after timestamp. Default=5000", default=5000)

    args = parser.parse_args()

    equity = onGetEquity(args.symbol, args.recvWindow)
    
    print("[Equity]", equity)