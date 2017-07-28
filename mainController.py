#!/user/bin/python
import wx
from loginController import LogIn
from databaseConn import DatabaseConn
from security import Security
from adminWindow import windowAdmin
from salePoint import windowSale

class mainControll(wx.Frame):
	"""docstring for mainControll"""
	def __init__(self, parent,id,title):
		super(mainControll, self).__init__(parent,title= title)
		panel = wx.Panel(self,-1)

		self.sales = windowSale(self)
		self.window = windowAdmin(self)
		self.login = LogIn(panel, -1)

		box = wx.BoxSizer()
		box.Add(self.login,1, wx.EXPAND | wx.ALL, 5)
		self.login.btnLogin.Bind(wx.EVT_BUTTON,self.showSalePane)
		self.login.passText.Bind(wx.EVT_KEY_UP ,self.enterkey)
		self.login.passNoText.Bind(wx.EVT_KEY_UP, self.enterkey)
		self.window.Bind(wx.EVT_CLOSE,self.closeAll)
		self.sales.Hide()
		self.window.Hide()
		self.sales.Bind(wx.EVT_CLOSE,self.closeAll)
		self.window.Bind(wx.EVT_MENU,self.OnClose)
		self.sales.Bind(wx.EVT_MENU,self.OnClose)
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
			self.sales.Close()
			self.Close()
		if id == wx.ID_ABORT:
			self.window.Hide()
			self.sales.Hide()
			self.Show()
			self.Layout()

	def closeAll(self,e):
		id = e.GetId()
		if id == wx.ID_CANCEL:
			self.Close()
			self.window.Close()
			self.sales.Close()
		if id == wx.ID_ABORT:
			self.window.Hide()
			self.sales.Hide()
			self.Show()
			self.Layout()

	def showSalePane(self,event):
		name = self.login.nameText.GetValue()
		user = Security(name,self.login.passText.GetValue())
		connect = DatabaseConn()
		connect.cur().execute("UPDATE security SET state = 'off'")
		data = connect.cur().execute("select name,password,status from security")
		if user.checkpass(data):
			if(user.getStatus()== 'admin'):
				connect.cur().execute("UPDATE security SET state = 'on'  WHERE name = '{name}'".format(name=name))
				connect.commit()
				self.login.nameText.SetValue("")
				self.login.passText.SetValue("")
				self.window.Show(True)
				self.Hide()
				self.Layout()
			else:
				connect.cur().execute("UPDATE security SET state = 'on'  WHERE name = '{name}'".format(name=name))
				connect.commit()
				self.login.nameText.SetValue("")
				self.login.passText.SetValue("")
				self.sales.Show()
				self.Hide()
				self.Layout()
		else:
			self.login.status.SetLabel("Incorrect Username or Password")
		connect.close()

def main():
	app = wx.App()
	mainControll(None, 1,'GMS - "Huduma Chap Chap"')
	app.MainLoop()

if __name__ == '__main__':
		main()