import wx 
class Frame1(wx.Frame):
 def __init__(self,superior):
        wx.Frame.__init__(self, parent = superior, title = "Example", pos= (200,200), size= (500,500))
        panel = wx.Panel(self)
        text1= wx.TextCtrl(panel, value = "Hello, World!", size = (200,100))
if __name__ == '__main__': 
    app =wx.App()
    frame = Frame1(None)
    frame.Show(True)
    app.MainLoop() 
