import wx

class Frame0(wx.Frame):
	def __init__(self, superior):
		wx.Frame.__init__(self, parent=superior, title='hihi')
		panel = wx.Panel(self)
		sizer = wx.BoxSizer(wx.VERTICAL)
		self.text1 = wx.TextCtrl(panel, value='Hello,World', size=(200,180), style=wx.TE_MULTILINE)
		sizer.Add(self.text1, 0,wx.ALIGN_TOP | wx.EXPAND)
		button = wx.Button(panel, label='Click me')
		sizer.Add(button)
		panel.SetSizerAndFit(sizer)
		panel.Layout()
		self.Bind(wx.EVT_BUTTON,self.OnClick,button)

	def OnClick(self, text):
		self.text1.AppendText('\nHello,World')

if __name__ == '__main__':
	app = wx.App()
	frame = Frame0(None)
	frame.Show()
app.MainLoop()