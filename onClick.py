import wx

class Frame0(wx.Frame):
	def __init__(self, superior):
		wx.Frame.__init__(self, parent=superior,title = "Example")
		self.panel = wx.Panel(self)
		self.panel.Bind(wx.EVT_LEFT_UP, self.onClick)
	
	def onClick(self, event):
		print("MouseUP")
		posm = event.GetPosition()
		wx.StaticText(parent=self.panel, label="hello,world", pos=(posm.x,posm.y))

if __name__ == "__main__":
	print("hi")
	app = wx.App()
	frame = Frame0(None)
	frame.Show(True)
	app.MainLoop()

