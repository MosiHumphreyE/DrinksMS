import sys
import wx
import datetime
from databaseConn import DatabaseConn
connection = DatabaseConn()
date = datetime.datetime.now()

class dailySaleReport(wx.Panel):
	def __init__(self,parent,id):
		wx.Panel.__init__(self,parent,id)
		sizer = wx.GridBagSizer(2,0)
		self.hbUp = wx.BoxSizer(wx.HORIZONTAL)
		sb = wx.StaticBox(self,-1,'DAILY SALES REPORT')
		box = wx.StaticBoxSizer(sb,wx.HORIZONTAL)
		self.choice = ['Daily Sales Report','Main Sales Report','Main Stock Report']
		self.choiceBox = wx.Choice(self,1,choices=self.choice,size=(150,35))
		self.hbUp.Add(self.choiceBox, wx.EXPAND, border = 5)
		st1= wx.StaticText(self,1,'')
		self.hbUp.Add(st1, wx.EXPAND,border = 5)
		st2 = wx.StaticText(self, 1, '')
		self.hbUp.Add(st2, wx.EXPAND, border=5)
		self.dailySale = wx.ListCtrl(self, -1, size = (1000,500),style=wx.LC_REPORT )
		self.dailySale.InsertColumn(0, 'Name', width=200)
		self.dailySale.InsertColumn(1, 'Quantity', wx.LIST_FORMAT_RIGHT, 200)
		self.dailySale.InsertColumn(2, 'Sales', wx.LIST_FORMAT_RIGHT, 200)
		self.dailySale.InsertColumn(3, 'Profit', wx.LIST_FORMAT_RIGHT, 200)
		box.Add(self.dailySale,flag=wx.EXPAND | wx.ALL,border=5)
		vdate = '{day}/{month}/{year}'.format(day=date.day,month=date.month,year=date.year)
		dateText = wx.StaticText(self, 1, vdate)
		self.btnCommit = wx.Button(self,-1,'Commit Daily Sales',size=(150,35))
		sizer.Add(self.btnCommit, pos=(3, 1), flag=wx.EXPAND | wx.ALL, border=5)
		sizer.Add(dateText,pos=(0,1),flag=wx.EXPAND | wx.ALL,border=5)
		sizer.Add(self.hbUp,pos=(0,0),flag=wx.EXPAND | wx.ALL,border=5)
		sizer.Add(box,pos=(2,0),flag=wx.EXPAND | wx.ALL,border=5)
		self.SetSizer(sizer)
		self.Fit()
		self.Show(True)

class mainSaleReport(wx.Panel):
	def __init__(self,parent,id):
		wx.Panel.__init__(self,parent,id)
		sizer = wx.GridBagSizer(2,0)
		self.hbUp = wx.BoxSizer(wx.HORIZONTAL)
		sb = wx.StaticBox(self,-1,'MAIN SALES REPORT')
		box = wx.StaticBoxSizer(sb,wx.HORIZONTAL)
		self.choice = ['Main Sales Report','Daily Sales Report','Main Stock Report']
		self.choiceBox = wx.Choice(self,1,choices=self.choice,size=(150,35))
		self.hbUp.Add(self.choiceBox, wx.EXPAND, border = 5)
		st1= wx.StaticText(self,1,'')
		self.hbUp.Add(st1, wx.EXPAND,border = 5)
		st2= wx.StaticText(self,1,'')
		self.hbUp.Add(st2, wx.EXPAND,border = 5)
		self.mainSale = wx.ListCtrl(self,-1,size = (1000,500),style=wx.LC_REPORT)
		self.mainSale.InsertColumn(0, 'Name', width=200)
		self.mainSale.InsertColumn(1, 'Quantity', wx.LIST_FORMAT_RIGHT, 200)
		self.mainSale.InsertColumn(2, 'Sales', wx.LIST_FORMAT_RIGHT, 200)
		self.mainSale.InsertColumn(3, 'Date', wx.LIST_FORMAT_RIGHT, 200)
		box.Add(self.mainSale,flag=wx.EXPAND | wx.ALL,border=5)
		vdate = '{day}/{month}/{year}'.format(day=date.day,month=date.month,year=date.year)
		dateText = wx.StaticText(self, 1, vdate)
		sizer.Add(dateText,pos=(0,1),flag=wx.EXPAND | wx.ALL,border=5)
		sizer.Add(self.hbUp,pos=(0,0),flag=wx.EXPAND | wx.ALL,border=5)
		sizer.Add(box,pos=(2,0),flag=wx.EXPAND | wx.ALL,border=5)
		self.SetSizer(sizer)
		self.Fit()
		self.Show(True)


class mainStockReport(wx.Panel):
	def __init__(self, parent, id):
		wx.Panel.__init__(self, parent, id)
		sizer = wx.GridBagSizer(2, 0)
		self.hbUp = wx.BoxSizer(wx.HORIZONTAL)
		sb = wx.StaticBox(self,-1,'MAIN STOCK REPORT')
		box = wx.StaticBoxSizer(sb,wx.HORIZONTAL)
		self.choice = [ 'Main Stock Report','Daily Sales Report', 'Main Sales Report']
		self.choiceBox = wx.Choice(self, 1, choices=self.choice,  size=(150, 35))
		self.hbUp.Add(self.choiceBox, wx.EXPAND, border=5)
		st1= wx.StaticText(self,1,'')
		self.hbUp.Add(st1, wx.EXPAND,border = 5)
		st2= wx.StaticText(self,1,'')
		self.hbUp.Add(st2, wx.EXPAND,border = 5)
		self.mainStock = wx.ListCtrl(self,-1,size = (1000,500),style=wx.LC_REPORT)
		self.mainStock.InsertColumn(0, 'Name', width=200)
		self.mainStock.InsertColumn(1, 'Quantity', wx.LIST_FORMAT_RIGHT, 200)
		self.mainStock.InsertColumn(2, 'Sale Cost', wx.LIST_FORMAT_RIGHT, 200)
		self.mainStock.InsertColumn(3, 'Purchase Cost', wx.LIST_FORMAT_RIGHT, 200)
		self.mainStock.InsertColumn(4, 'Date', wx.LIST_FORMAT_RIGHT, 200)
		box.Add(self.mainStock,flag=wx.EXPAND | wx.ALL,border=5)
		vdate = '{day}/{month}/{year}'.format(day=date.day,month=date.month,year=date.year)
		dateText = wx.StaticText(self, 1, vdate)
		sizer.Add(dateText,pos=(0,1),flag=wx.EXPAND | wx.ALL,border=5)
		sizer.Add(self.hbUp,pos=(0,0),flag=wx.EXPAND | wx.ALL,border=5)
		sizer.Add(box,pos=(2,0),flag=wx.EXPAND | wx.ALL,border=5)
		self.SetSizer(sizer)
		self.Fit()
		self.Show(True)

class report(wx.Panel):
	def __init__(self, parent, id):
		super(report, self).__init__(parent, id)
		self.hbDown = wx.BoxSizer()
		self.dailySaleReport = dailySaleReport(self,-1)
		self.mainSaleReport = mainSaleReport(self,-1)
		self.mainStockReport = mainStockReport(self,-1)
		self.hbDown.Add(self.dailySaleReport,1, flag=wx.EXPAND | wx.ALL, border=5)
		self.hbDown.Add(self.mainSaleReport, 1,flag=wx.EXPAND | wx.ALL, border=5)
		self.hbDown.Add(self.mainStockReport,1, flag=wx.EXPAND | wx.ALL, border=5)
		self.mainSaleReport.Hide()
		self.mainStockReport.Hide()
		self.dailySaleReport.choiceBox.Bind(wx.EVT_CHOICE,self.OnClick)
		self.dailySaleReport.btnCommit.Bind(wx.EVT_BUTTON,self.commit)
		self.mainSaleReport.choiceBox.Bind(wx.EVT_CHOICE,self.OnClick1)
		self.mainStockReport.choiceBox.Bind(wx.EVT_CHOICE,self.OnClick2)
		self.SetSizer(self.hbDown)
		self.Centre()
		self.Show(True)
	# we are committing todays sales
	def commit(self,e):
		for row in connection.cur().execute('SELECT name,quantity FROM dailySale WHERE quantity != 0'):
			quantity = connection.cur().execute("SELECT quantity FROM mainStock WHERE name = '{name}'".format(name=row[0]))
			try:
				Mainqua = int(quantity.next()[0])
				salequa=int(row[1])
				remainder = Mainqua - salequa
				 # Cheking to see if data is ok between today's Sales and main sales
				if remainder>=0:
					connection.cur().execute("UPDATE mainStock SET quantity = {qua} WHERE name = '{name}'".format(name=row[0], qua=str(remainder)))
					connection.cur().execute("INSERT INTO mainSale (name,quantity,sales,profit,date) "
											 "SELECT name,quantity,sales,profit,date FROM dailySale where name = '{name}'".format(name=row[0]))
					connection.cur().execute("UPDATE dailySale SET quantity=0,sales=0,profit=0 WHERE name = '{name}'".format(name=row[0]))
				else:
					connection.commit()
					wx.MessageBox("{name} quantity out of Stock: \nMainstock quantity ={qua}\nToday's sales quantity ={todaySale}"
								  .format(name = row[0],qua=Mainqua,todaySale=salequa))
					break
			except ValueError:
				wx.MessageBox('Something went wrong somewhere')
		self.refresh()

	def OnClick(self,evt):
		if (self.dailySaleReport.choiceBox.GetString(self.dailySaleReport.choiceBox.GetSelection()) =='Main Sales Report'):
			self.mainSaleReport.Show()
			self.dailySaleReport.Hide()
			self.Layout()
		if (self.dailySaleReport.choiceBox.GetString(self.dailySaleReport.choiceBox.GetSelection()) =='Main Stock Report'):
			self.mainStockReport.Show()
			self.dailySaleReport.Hide()
			self.Layout()

	def OnClick1(self,evt):
		if (self.mainSaleReport.choiceBox.GetString(self.mainSaleReport.choiceBox.GetSelection()) =='Daily Sales Report'):
			self.dailySaleReport.Show()
			self.mainSaleReport.Hide()
			self.Layout()
		if(self.mainSaleReport.choiceBox.GetString(self.mainSaleReport.choiceBox.GetSelection()) =='Main Stock Report'):
			self.mainStockReport.Show()
			self.mainSaleReport.Hide()
			self.Layout()
	def OnClick2(self,evt):
		if (self.mainStockReport.choiceBox.GetString(self.mainStockReport.choiceBox.GetSelection()) =='Daily Sales Report'):
			self.dailySaleReport.Show()
			self.mainStockReport.Hide()
			self.Layout()
		if (self.mainStockReport.choiceBox.GetString(self.mainStockReport.choiceBox.GetSelection()) =='Main Sales Report'):
			self.mainSaleReport.Show()
			self.mainStockReport.Hide()
			self.Layout()

	def refresh(self):
		self.mainSaleReport.mainSale.DeleteAllItems()
		self.mainSaleReport.mainSaleData = [row for row in connection.cur().execute(
			'SELECT name,quantity,sales,date FROM mainSale ORDER BY date ASC')]
		for i in self.mainSaleReport.mainSaleData:
			index = self.mainSaleReport.mainSale.InsertStringItem(sys.maxint, i[0])
			self.mainSaleReport.mainSale.SetStringItem(index, 1, str(i[1]))
			self.mainSaleReport.mainSale.SetStringItem(index, 2, str(i[2]))
			self.mainSaleReport.mainSale.SetStringItem(index, 3, i[3])
		self.dailySaleReport.dailySale.DeleteAllItems()



		for i in connection.cur().execute("SELECT name,quantity,sales,profit FROM dailySale ORDER BY quantity DESC"):
			index = self.dailySaleReport.dailySale.InsertStringItem(sys.maxint, i[0])
			self.dailySaleReport.dailySale.SetStringItem(index, 1, str(i[1]))
			self.dailySaleReport.dailySale.SetStringItem(index, 2, str(i[2]))
			self.dailySaleReport.dailySale.SetStringItem(index, 3, str(i[3]))
		self.mainStockReport.mainStock.DeleteAllItems()


		self.mainStockReport.mainStockData = [row for row in connection.cur().execute(
			'SELECT name,quantity,date,saleCost,purCost FROM mainStock')]
		for i in self.mainStockReport.mainStockData:
			index = self.mainStockReport.mainStock.InsertStringItem(sys.maxint, i[0])
			self.mainStockReport.mainStock.SetStringItem(index, 1, str(i[1]))
			self.mainStockReport.mainStock.SetStringItem(index, 2, str(i[3]))
			self.mainStockReport.mainStock.SetStringItem(index, 3, str(i[4]))
			self.mainStockReport.mainStock.SetStringItem(index, 4,i[2])