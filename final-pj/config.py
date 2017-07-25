import wx
import wx.adv
from datetime import date
from datetime import timedelta
import numpy as np

import myPK.plotingDG as dg





# stockURL = urlopen(api.BASE + api.OP_SIZE + 'compact' + api.SYMBOL + 'DD' + api.API_KEY)
# resp = json.load(stockURL)

# for stock in resp['Time Series (Daily)'].items():
# 	print(stock[0], stock[1]['1. open'])
# print('hihi')

# class confFrame(wx.Frame):
# 	def __init__(self, superior):
# 		print('okkkk')
# 		print(stoSym)
# 		wx.Frame.__init__(self, parent=superior, title='Configuration')
# 		self.panel = wx.Panel(self)
# 		self.startDay = []
# 		self.endDay =[]
# 		self.mask = np.array([False, False, False, False, False])

# 		dr_lbl = wx.StaticText(self.panel, label='Data Range')
# 		sd_lbl = wx.StaticText(self.panel, label='Start date')
# 		self.sd_dpc = wx.adv.DatePickerCtrl(self.panel, style=wx.adv.DP_DROPDOWN)
# 		ed_lbl = wx.StaticText(self.panel, label='End date')
# 		self.ed_dpc = wx.adv.DatePickerCtrl(self.panel, style=wx.adv.DP_DROPDOWN)
# 		self.Bind(wx.adv.EVT_DATE_CHANGED, self.GetStartDate, self.sd_dpc)
# 		self.Bind(wx.adv.EVT_DATE_CHANGED, self.GetEndDate, self.ed_dpc)

# 		ds_lbl = wx.StaticText(self.panel, label='Data Set')
# 		self.open_cb = wx.CheckBox(self.panel, label='open')
# 		self.close_cb = wx.CheckBox(self.panel, label='close')
# 		self.high_cb = wx.CheckBox(self.panel, label='high')
# 		self.low_cb = wx.CheckBox(self.panel, label='low')
# 		self.vol_cb = wx.CheckBox(self.panel, label='volume')
# 		self.Bind(wx.EVT_CHECKBOX, self.opCK, self.open_cb)
# 		self.Bind(wx.EVT_CHECKBOX, self.clCK, self.close_cb)
# 		self.Bind(wx.EVT_CHECKBOX, self.hgCK, self.high_cb)
# 		self.Bind(wx.EVT_CHECKBOX, self.lwCK, self.low_cb)
# 		self.Bind(wx.EVT_CHECKBOX, self.volCK, self.vol_cb)
		

# 		ok_btn = wx.Button(self.panel, label='Ok')
# 		can_btn = wx.Button(self.panel, label='Cancel')
# 		self.Bind(wx.EVT_BUTTON, self.GenPlot, ok_btn)
# 		self.Bind(wx.EVT_BUTTON, self.Cancel, can_btn)

# 		drSizer = wx.BoxSizer(wx.VERTICAL)
# 		drSizer.Add(dr_lbl, 0, wx.ALL, 5)
# 		drSizer.Add(wx.StaticLine(self.panel), 0, wx.ALL, 5)
# 		drSizer.Add(sd_lbl, 0, wx.ALL, 5)
# 		drSizer.Add(self.sd_dpc, 0, wx.ALL, 5)
# 		drSizer.Add(ed_lbl, 0, wx.ALL, 5)
# 		drSizer.Add(self.ed_dpc, 0, wx.ALL, 5)

# 		dsSizer = wx.BoxSizer(wx.VERTICAL)
# 		dsSizer.Add(ds_lbl, 0, wx.ALL, 5)
# 		dsSizer.Add(wx.StaticLine(self.panel), 0, wx.ALL, 5)
# 		dsSizer.Add(self.open_cb, 0, wx.ALL, 5)
# 		dsSizer.Add(self.close_cb, 0, wx.ALL, 5)
# 		dsSizer.Add(self.high_cb, 0, wx.ALL, 5)
# 		dsSizer.Add(self.low_cb, 0, wx.ALL, 5)
# 		dsSizer.Add(self.vol_cb, 0, wx.ALL, 5)

# 		midSizer = wx.BoxSizer(wx.HORIZONTAL)
# 		midSizer.Add(drSizer, 0, wx.ALL, 5)
# 		midSizer.Add(dsSizer, 0, wx.ALL, 5)

# 		lowSizer = wx.BoxSizer(wx.HORIZONTAL)
# 		lowSizer.Add(ok_btn, 0, wx.ALL, 5)
# 		lowSizer.Add(can_btn, 0, wx.ALL, 5)

# 		fullSizer = wx.BoxSizer(wx.VERTICAL)
# 		fullSizer.Add(midSizer, 0, wx.ALL, 5)
# 		fullSizer.Add(lowSizer, 0, wx.ALL, 5)

# 		self.panel.SetSizer(fullSizer)
# 		fullSizer.Fit(self)

# 	def showDG(self, code1):
# 		self.code = code1
# 		self.Show(True)

# 	def GetStartDate(self, event):
# 		self.startDay = self.sd_dpc.GetValue().FormatISODate()

# 	def GetEndDate(self, event):
# 		self.endDay = self.ed_dpc.GetValue().FormatISODate()
		
# 	def opCK(self, event):
# 		self.mask[0] = self.open_cb.IsChecked()
# 		print(self.mask)

# 	def clCK(self, event):
# 		self.mask[1] = self.close_cb.IsChecked()
# 		print(self.mask)

# 	def hgCK(self, event):
# 		self.mask[2] = self.high_cb.IsChecked() 
# 		print(self.mask)

# 	def lwCK(self, event):
# 		self.mask[3] = self.low_cb.IsChecked()
# 		print(self.mask)

# 	def volCK(self, event):
# 		self.mask[4] = self.vol_cb.IsChecked()
# 		print(self.mask)



# 	def GenPlot(self, event):
# 		if not self.startDay or not self.endDay:
# 			td = date.today()
# 			dates = [str(td),str(td + timedelta(days=-30))]
# 		else:
# 			dates = [self.startDay,self.endDay]

# 		stoSym = 'DD'
# 		dg.Ploting(self.mask, stoSym, dates)

# 	def Cancel(self, event):
# 		self.Close()


def ConfSST(stoSym):
	print('ccsst')
	# app = wx.App()
	# frame = confFrame(None)
	# frame.showDG(stoSym)
	# app.MainLoop()

