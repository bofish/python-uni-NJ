import wx
from urllib.request import urlopen
import json
import myPK.config as cf

# crate main view
class mainFrame(wx.Frame):
	def __init__(self,superior):
		wx.Frame.__init__(self, parent=superior, title='Dow Jones Stock')
		self.panel = wx.Panel(self)

		search_label = wx.StaticText(self.panel, label='Stock Code:')
		search_input = wx.TextCtrl(self.panel)
		
		self.stockls = wx.ListCtrl(self.panel, size=(-1,500), style=wx.LC_REPORT)
		self.stockls.InsertColumn(0, 'Symbol')
		self.stockls.InsertColumn(1, 'Name', width=200)
		self.stockls.InsertColumn(2, 'FTM')
		self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.StoClick, self.stockls)


		quit_btn = wx.Button(self.panel, label='Quit')
		re_btn = wx.Button(self.panel, label='Refresh')
		self.Bind(wx.EVT_BUTTON, self.Quit, quit_btn)
		self.Bind(wx.EVT_BUTTON, self.Refresh, re_btn)


		topSizer = wx.BoxSizer(wx.VERTICAL)
		searchSizer = wx.BoxSizer(wx.HORIZONTAL)
		tableSizer = wx.BoxSizer(wx.HORIZONTAL)
		btnSizer = wx.BoxSizer(wx.HORIZONTAL)

		searchSizer.Add(search_label, 0, wx.ALL, 5)
		searchSizer.Add(search_input, 0, wx.ALL|wx.EXPAND, 5)

		tableSizer.Add(self.stockls, 1, wx.ALL|wx.EXPAND, 5)

		btnSizer.Add(quit_btn, 0, wx.ALL, 5)
		btnSizer.Add(re_btn, 0, wx.ALL, 5)

		topSizer.Add(searchSizer, 0, wx.ALL|wx.EXPAND, 5)
		topSizer.Add(tableSizer, 0, wx.ALL|wx.EXPAND, 5)
		topSizer.Add(btnSizer, 0, wx.ALL|wx.EXPAND, 5)

		self.panel.SetSizer(topSizer)
		topSizer.Fit(self)


	def Quit(self, event):
		self.Close()

	def Refresh(self, event):
		url = urlopen('http://query1.finance.yahoo.com/v7/finance/quote?formatted=true&crumb=azVqAvrYffI&lang=en-US&region=US&symbols=DD%2CAAPL%2CCSCO%2CCVX%2CVZ%2CJPM%2CJNJ%2CMRK%2CPFE%2CUNH%2CMSFT%2CIBM%2CV%2CUTX%2CTRV%2CGE%2CKO%2CNKE%2CGS%2CMMM%2CDIS%2CMCD%2CINTC%2CCAT%2CPG%2CXOM%2CAXP%2CHD%2CBA%2CWMT&fields=longName%2CregularMarketPrice%2CregularMarketChange%2CregularMarketChangePercent&corsDomain=finance.yahoo.com')
		resp = json.load(url)

		for index, stock in enumerate(resp['quoteResponse']['result']):
			self.stockls.InsertItem(index, stock['symbol'])
			self.stockls.SetItem(index, 1, stock['longName'])
			self.stockls.SetItem(index, 2, stock['regularMarketPrice']['fmt'])

	def StoClick(self, event):
		print('yayaya')
		
		count = event.GetIndex()
		stoSymbol = self.stockls.GetItem(itemIdx=count).GetText()
		# print(stoSymbol)
		if __name__ == '__main__':
			cf.ConfSST(stoSymbol)
		


if __name__ == '__main__':
	app = wx.App()
	frame = mainFrame(None)
	frame.Refresh(None)
	frame.Show()
	app.MainLoop()


		