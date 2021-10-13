from main import API_SECRET, API_ENDPOINT, API_KEY, _getSignature, _getCurrentTime, _printJson
import requests, argparse

def onSendOrder(symbol, quantity, side, type, positionSide, recvWindow, timestamp):
    ''' Send order with the input data '''
    param = "symbol=%s&quantity=%s&side=%s&type=%s&positionSide=%s&recvWindow=%s&timestamp=%s" % (symbol, quantity, side, type, positionSide, recvWindow, timestamp);
    signature = _getSignature(param, API_SECRET)
    param += "&signature=" + signature

    res = requests.post(API_ENDPOINT + '/v1/order?' + param, data = {}, headers={
        'Content-Type': 'application/json',
        'X-MBX-APIKEY': API_KEY
    }).json()
    return res

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument("-s", "--symbol", help="Input symbol", required=True)
    parser.add_argument("-q", "--quantity", help="Quantitity to trade. Default=1", required=True)
    parser.add_argument("-d", "--side", help="Either BUY or SELL. Default=BUY", choices=['BUY', 'SELL'], default='BUY')
    parser.add_argument("-t", "--type", help="Trade type. Default=MARKET", choices=['LIMIT', 'MARKET', 'STOP', 'STOP_MARKET', 'TAKE_PROFIT', 'TAKE_PROFIT_MARKET', 'TRAILING_STOP_MARKET'], default='MARKET')
    parser.add_argument('-p', '--position', help="Position side. Default=BOTH", choices=['BOTH', 'LONG', 'SHORT'], default='BOTH')
    parser.add_argument('-w', '--recvWindow', help="Processing milliseconds after timestamp. Default=5000", default=5000)

    args = parser.parse_args()

    res = onSendOrder(args.symbol, args.quantity, args.side, args.type, args.position, args.recvWindow, _getCurrentTime())
    _printJson(res)