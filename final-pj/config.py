import wx
import wx.adv
import API_URL as api
from urllib.request import urlopen
import json



# stockURL = urlopen(api.BASE + api.OP_SIZE + 'compact' + api.SYMBOL + 'DD' + api.API_KEY)
# resp = json.load(stockURL)

# for stock in resp['Time Series (Daily)'].items():
# 	print(stock[0], stock[1]['1. open'])


class confFrame(wx.Frame):
	def __init__(self, superior):
		wx.Frame.__init__(self, parent=superior, title='Configuration')
		self.panel = wx.Panel(self)

		dr_lbl = wx.StaticText(self.panel, label='Data Range')
		sd_lbl = wx.StaticText(self.panel, label='Start date')
		sd_dpc = wx.adv.DatePickerCtrl(self.panel, style=wx.adv.DP_DROPDOWN)
		ed_lbl = wx.StaticText(self.panel, label='End date')
		ed_dpc = wx.adv.DatePickerCtrl(self.panel, style=wx.adv.DP_DROPDOWN)

		ds_lbl = wx.StaticText(self.panel, label='Data Set')
		open_cb = wx.CheckBox(self.panel, label='open')
		close_cb = wx.CheckBox(self.panel, label='close')
		high_cb = wx.CheckBox(self.panel, label='high')
		low_cb = wx.CheckBox(self.panel, label='low')
		vol_cb = wx.CheckBox(self.panel, label='volume')

		ok_btn = wx.Button(self.panel, label='Ok')
		can_btn = wx.Button(self.panel, label='Cancel')
		self.Bind(wx.EVT_BUTTON, self.GenPlot, ok_btn)
		self.Bind(wx.EVT_BUTTON, self.Cancel, can_btn)

		drSizer = wx.BoxSizer(wx.VERTICAL)
		drSizer.Add(dr_lbl, 0, wx.ALL, 5)
		drSizer.Add(wx.StaticLine(self.panel), 0, wx.ALL, 5)
		drSizer.Add(sd_lbl, 0, wx.ALL, 5)
		drSizer.Add(sd_dpc, 0, wx.ALL, 5)
		drSizer.Add(ed_lbl, 0, wx.ALL, 5)
		drSizer.Add(ed_dpc, 0, wx.ALL, 5)

		dsSizer = wx.BoxSizer(wx.VERTICAL)
		dsSizer.Add(ds_lbl, 0, wx.ALL, 5)
		dsSizer.Add(wx.StaticLine(self.panel), 0, wx.ALL, 5)
		dsSizer.Add(open_cb, 0, wx.ALL, 5)
		dsSizer.Add(close_cb, 0, wx.ALL, 5)
		dsSizer.Add(high_cb, 0, wx.ALL, 5)
		dsSizer.Add(low_cb, 0, wx.ALL, 5)
		dsSizer.Add(vol_cb, 0, wx.ALL, 5)

		midSizer = wx.BoxSizer(wx.HORIZONTAL)
		midSizer.Add(drSizer, 0, wx.ALL, 5)
		midSizer.Add(dsSizer, 0, wx.ALL, 5)

		lowSizer = wx.BoxSizer(wx.HORIZONTAL)
		lowSizer.Add(ok_btn, 0, wx.ALL, 5)
		lowSizer.Add(can_btn, 0, wx.ALL, 5)

		fullSizer = wx.BoxSizer(wx.VERTICAL)
		fullSizer.Add(midSizer, 0, wx.ALL, 5)
		fullSizer.Add(lowSizer, 0, wx.ALL, 5)

		self.panel.SetSizer(fullSizer)
		fullSizer.Fit(self)

	def GenPlot(self, event):
		pass

	def Cancel(self, event):
		self.Close()


if __name__ == '__main__':
	app = wx.App()
	frame = confFrame(None)
	frame.Show()
	app.MainLoop()

