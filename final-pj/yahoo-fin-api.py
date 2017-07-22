from urllib.request import urlopen
import json

url = urlopen('http://query1.finance.yahoo.com/v7/finance/quote?formatted=true&crumb=azVqAvrYffI&lang=en-US&region=US&symbols=DD%2CAAPL%2CCSCO%2CCVX%2CVZ%2CJPM%2CJNJ%2CMRK%2CPFE%2CUNH%2CMSFT%2CIBM%2CV%2CUTX%2CTRV%2CGE%2CKO%2CNKE%2CGS%2CMMM%2CDIS%2CMCD%2CINTC%2CCAT%2CPG%2CXOM%2CAXP%2CHD%2CBA%2CWMT&fields=longName%2CregularMarketPrice%2CregularMarketChange%2CregularMarketChangePercent&corsDomain=finance.yahoo.com')
resp = json.loads(url.read().decode('utf-8'))
for stock in resp['quoteResponse']['result']:
    print(stock['symbol'], stock['longName'], stock['regularMarketPrice']['fmt'])