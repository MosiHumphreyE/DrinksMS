#!/user/bin/python
import wx
from loginController import LogIn
from  saleController import Content
from databaseConn import DatabaseConn
from security import Security
from adminWindow import windowAdmin

class mainControll(wx.Frame):
	"""docstring for mainControll"""
	def __init__(self, parent,id,title):
		super(mainControll, self).__init__(parent,title= title)
		panel = wx.Panel(self,-1)

		self.login = LogIn(panel, -1)
		self.sales = Content(panel,-1)
		self.window = windowAdmin(self)
		box = wx.BoxSizer()
		box.Add(self.login,1, wx.EXPAND | wx.ALL, 5)
		box.Add(self.sales,1,wx.EXPAND | wx.ALL,5)
		box.Add(self.window,1,wx.EXPAND | wx.ALL,5)
		self.login.btnLogin.Bind(wx.EVT_BUTTON,self.showSalePane)
		self.login.passText.Bind(wx.EVT_KEY_DOWN ,self.enterkey)
		self.login.passNoText.Bind(wx.EVT_KEY_DOWN, self.enterkey)
		self.window.Bind(wx.EVT_CLOSE,self.closeAll)
		self.sales.Hide()
		self.window.Hide()
		self.window.Bind(wx.EVT_MENU,self.OnClose)
		panel.SetSizer(box)
		self.Maximize(True)
		self.Show()

	def enterkey(self, event):
		keycode = event.GetKeyCode()
		if keycode == wx.WXK_RETURN or keycode == wx.WXK_NUMPAD_ENTER:
			self.showSalePane(event=None)
			event.EventObject.Navigate()
		event.Skip()

	def OnClose(self,e):
		id = e.GetId()
		if id == wx.ID_EXIT:
			self.window.Close()
			self.Close()

	def closeAll(self,e):
		id = e.GetId()
		if id == wx.ID_CANCEL:
			print"heloo"
			self.Close()
			self.window.Close()

	def showSalePane(self,event):
		user = Security(self.login.nameText.GetValue(),self.login.passText.GetValue())
		connect = DatabaseConn()
		data = connect.cur().execute("select name,password,status from security")
		if user.checkpass(data):
			if(user.getStatus()== 'admin'):
				self.window.Show(True)
				self.Hide()
				self.Layout()
			else:
				self.sales.Show()
				self.window.Hide()
				self.login.Hide()
				self.Layout()
		else:
			self.login.status.SetLabel("Wrong Password")
		connect.close()

def main():
	app = wx.App()
	mainControll(None, 1,'Drinks Management System')
	app.MainLoop()

if __name__ == '__main__':
		main()