# binance-trade-python
https://testnet.binancefuture.com/en/futures/BTCUSDT
https://binance-docs.github.io/apidocs/testnet/en/#change-log

# Send Order
python sendOrder.py -s BTCUSDT -q 1 -d BUY -t MARKET -p BOTH -w 10000
python getBalance.py  -s BTCUSDT -w 10000
python getEquity.py -s BTCUSDT -w 10000
python getFreeMargin.py