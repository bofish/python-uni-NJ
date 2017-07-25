import numpy as np
import pandas as pd
import matplotlib as mpl
from urllib.request import urlopen
import json
import myPK.API_URL as api



def max(a, b):
    return a if a > b else b

def Ploting(mask, stoSym, dates):
	# print('hihihi')

	# mask = np.array([True, True, False, False, True])
	# stoSym = 'DD'
	# dates = ['2017-07-01','2017-06-21']

	stockURL = urlopen(api.BASE + api.OP_SIZE + 'full' + api.SYMBOL + stoSym + api.API_KEY)
	resp = json.load(stockURL)
	emptyArr = np.array([[0,0,0,0,0]])
	dateArr = np.array([])
	indexArr = np.array(['Open', 'Close', 'High', 'Low', 'Volume'])
	for stock in resp['Time Series (Daily)'].items():
	    emptyArr = np.append(emptyArr, [[float(stock[1]['1. open']), float(stock[1]['4. close']), float(stock[1]['2. high']), float(stock[1]['3. low']), float(stock[1]['6. volume'])]],axis=0)
	    dateArr = np.append(dateArr, stock[0])
	df = pd.DataFrame(data=emptyArr[1:,0:], index=dateArr, columns=indexArr)

	df_op = df.loc[dates[0]:dates[1]]
	df_op.plot(y=indexArr[mask])
	mpl.pyplot.show()



