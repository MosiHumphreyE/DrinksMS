#!/user/bin/python
import wx
from loginController import LogIn
from  saleController import Content
from databaseConn import DatabaseConn
from security import Security


class mainControll(wx.Frame):
	"""docstring for mainControll"""
	def __init__(self, parent,id,title):
		super(mainControll, self).__init__(parent,title= title)
		panel = wx.Panel(self,-1)

		self.menuBar()
		self.login = LogIn(panel, -1)
		self.sales = Content(panel,-1)

		box = wx.BoxSizer()
		box.Add(self.login,1, wx.EXPAND | wx.ALL, 5)
		box.Add(self.sales,1,wx.EXPAND | wx.ALL,5)
		self.login.btnLogin.Bind(wx.EVT_BUTTON,self.showSalePane)
		self.sales.Hide()
		panel.SetSizer(box)
		self.Maximize(True)
		self.Show()

	def menuBar(self):
		menubar = wx.MenuBar()
		file = wx.Menu()
		filehelp = wx.Menu()
		fileabout = wx.Menu()

		new = file.Append(wx.ID_NEW, 'New','New Session')
		file.AppendSeparator()
		exit = file.Append(wx.ID_EXIT,'Quit','Quit Application')

		about = fileabout.Append(wx.ID_ABOUT, 'About','About Application')
		fhelp = filehelp.Append(wx.ID_HELP,'Help','Help')
		menubar.Append(file,'&File')
		menubar.Append(fileabout,'&About')
		menubar.Append(filehelp,'&Help')
		self.SetMenuBar(menubar)

	def OnClose(self,e):
		self.Close()

	def showSalePane(self,e):
		user = Security(self.login.nameText.GetValue(),self.login.passText.GetValue())
		connect = DatabaseConn()
		data = connect.cur().execute("select name,password,status from security")
		if (user.checkpass(data)):
			self.sales.Show()
			self.login.Hide()
			self.Layout()
		else:
			self.login.status.SetLabelText("Wrong Password")
		connect.close()

		

def main():
	app = wx.App()
	mainControll(None, 1,'Drinks Management System')
	app.MainLoop()

if __name__ == '__main__':
		main()	
		