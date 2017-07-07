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
		self.choiceBox = wx.Choice(self,1,choices=self.choice,style = wx.CB_READONLY,size=(150,35))
		self.hbUp.Add(self.choiceBox, wx.EXPAND, border = 5)
		st1= wx.StaticText(self,1,'')
		self.hbUp.Add(st1, wx.EXPAND,border = 5)
		st2 = wx.StaticText(self, 1, '')
		self.hbUp.Add(st2, wx.EXPAND, border=5)

		self.dailySale = wx.ListCtrl(self, -1, size = (1000,500),style=wx.LC_REPORT )
		self.dailySale.InsertColumn(0, 'Name', width=200)
		self.dailySale.InsertColumn(1, 'Quantity', wx.LIST_FORMAT_RIGHT, 200)
		self.dailySale.InsertColumn(2, 'Type', wx.LIST_FORMAT_RIGHT, 200)
		self.dailySale.InsertColumn(3, 'Cost', wx.LIST_FORMAT_RIGHT, 200)
		self.dailySaleData =[row for row in connection.cur()
			.execute('SELECT name,quantity,type,cost  FROM dailySale')]
		for i in self.dailySaleData:
		 	index = self.dailySale.InsertStringItem(sys.maxint, i[0])
		 	self.dailySale.SetStringItem(index, 1, str(i[1]))
			self.dailySale.SetStringItem(index, 2, i[2])
			self.dailySale.SetStringItem(index, 3, str(i[3]))
		box.Add(self.dailySale,flag=wx.EXPAND | wx.ALL,border=5)

		vdate = '{day}/{month}/{year}'.format(day=date.day,month=date.month,year=date.year)
		dateText = wx.StaticText(self, 1, vdate)
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

		self.choice = ['Daily Sales Report','Main Sales Report','Main Stock Report']
		self.choiceBox = wx.Choice(self,1,choices=self.choice,style = wx.CB_READONLY,size=(150,35))
		self.hbUp.Add(self.choiceBox, wx.EXPAND, border = 5)
		st1= wx.StaticText(self,1,'')
		self.hbUp.Add(st1, wx.EXPAND,border = 5)
		st2= wx.StaticText(self,1,'')
		self.hbUp.Add(st2, wx.EXPAND,border = 5)

		self.mainSale = wx.ListCtrl(self,-1,size = (1000,500),style=wx.LC_REPORT)
		self.mainSale.InsertColumn(0, 'Name', width=200)
		self.mainSale.InsertColumn(1, 'Quantity', wx.LIST_FORMAT_RIGHT, 200)
		self.mainSale.InsertColumn(2, 'Type', wx.LIST_FORMAT_RIGHT, 200)
		self.mainSale.InsertColumn(3, 'Cost', wx.LIST_FORMAT_RIGHT, 200)
		self.mainSale.InsertColumn(4, 'Date', wx.LIST_FORMAT_RIGHT, 200)
		self.mainSaleData =[row for row in connection.cur().
			execute('SELECT name,quantity,type,cost,date FROM mainSale')]
		for i in self.mainSaleData:
		 	index = self.mainSale.InsertStringItem(sys.maxint, i[0])
		 	self.mainSale.SetStringItem(index, 1, str(i[1]))
		 	self.mainSale.SetStringItem(index, 2, i[2])
			self.mainSale.SetStringItem(index, 3, str(i[3]))
			self.mainSale.SetStringItem(index, 4, i[4])
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

		self.choice = ['Daily Sales Report', 'Main Sales Report', 'Main Stock Report']
		self.choiceBox = wx.Choice(self, 1, choices=self.choice, style=wx.CB_READONLY, size=(150, 35))
		self.hbUp.Add(self.choiceBox, wx.EXPAND, border=5)
		st1= wx.StaticText(self,1,'')
		self.hbUp.Add(st1, wx.EXPAND,border = 5)
		st2= wx.StaticText(self,1,'')
		self.hbUp.Add(st2, wx.EXPAND,border = 5)

		self.mainStock = wx.ListCtrl(self,-1,size = (1000,500),style=wx.LC_REPORT)
		self.mainStock.InsertColumn(0, 'Name', width=200)
		self.mainStock.InsertColumn(1, 'Quantity', wx.LIST_FORMAT_RIGHT, 200)
		self.mainStock.InsertColumn(2, 'Type', wx.LIST_FORMAT_RIGHT, 200)
		self.mainStock.InsertColumn(3, 'Cost@Drink', wx.LIST_FORMAT_RIGHT, 200)
		self.mainStock.InsertColumn(4, 'Date', wx.LIST_FORMAT_RIGHT, 200)
		box.Add(self.mainStock,flag=wx.EXPAND | wx.ALL,border=5)
		self.mainStockData =[row for row in connection.cur().execute('SELECT name,quantity,type,costperdrink,date  FROM mainStock')]
		for i in self.mainStockData:
			index = self.mainStock.InsertStringItem(sys.maxint, i[0])
		 	self.mainStock.SetStringItem(index, 1, str(i[1]))
			self.mainStock.SetStringItem(index, 2, i[2])
			self.mainStock.SetStringItem(index, 3, str(i[3]))
			self.mainStock.SetStringItem(index, 4, i[4])
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
		self.mainSaleReport.choiceBox.Bind(wx.EVT_CHOICE,self.OnClick1)
		self.mainStockReport.choiceBox.Bind(wx.EVT_CHOICE,self.OnClick2)
		self.SetSizer(self.hbDown)
		self.Centre()
		self.Show(True)

	def OnClick(self,evt):
		if (self.dailySaleReport.choiceBox.GetString(self.dailySaleReport.choiceBox.GetSelection()) =='Main Sales Report'):
			self.mainSaleReport.mainSaleData = [row for row in connection.cur().
				execute('SELECT name,quantity,type,cost,date FROM mainSale')]
			self.mainSaleReport.Show()
			self.dailySaleReport.Hide()
			self.Layout()

		if (self.dailySaleReport.choiceBox.GetString(self.dailySaleReport.choiceBox.GetSelection()) =='Main Stock Report'):
			self.mainStockReport.mainStockData = [row for row in connection.cur().execute(
				'SELECT name,quantity,type,costperdrink,date  FROM mainStock')]
			self.mainStockReport.Show()
			self.dailySaleReport.Hide()
			#self.Layout()

	def OnClick1(self,evt):
		if (self.mainSaleReport.choiceBox.GetString(self.mainSaleReport.choiceBox.GetSelection()) =='Daily Sales Report'):
			self.dailySaleReport.dailySale.DeleteAllItems()
			self.dailySaleReport.dailySaleData = [row for row in connection.cur()
				.execute('SELECT name,quantity,type,cost  FROM dailySale')]
			for i in self.dailySaleReport.dailySaleData:
				index = self.dailySaleReport.dailySale.InsertStringItem(sys.maxint, i[0])
				self.dailySaleReport.dailySale.SetStringItem(index, 1, str(i[1]))
				self.dailySaleReport.dailySale.SetStringItem(index, 2, i[2])
				self.dailySaleReport.dailySale.SetStringItem(index, 3, str(i[3]))
			self.dailySaleReport.Show()
			self.mainSaleReport.Hide()
			self.Layout()

		if(self.mainSaleReport.choiceBox.GetString(self.mainSaleReport.choiceBox.GetSelection()) =='Main Stock Report'):
			self.mainStockReport.mainStockData = [row for row in connection.cur().execute(
				'SELECT name,quantity,type,costperdrink,date  FROM mainStock')]
			self.mainStockReport.Show()
			self.mainSaleReport.Hide()
			self.Layout()

	def OnClick2(self,evt):
		if (self.mainStockReport.choiceBox.GetString(self.mainStockReport.choiceBox.GetSelection()) =='Daily Sales Report'):
			self.dailySaleReport.dailySale.DeleteAllItems()
			self.dailySaleReport.dailySaleData = [row for row in connection.cur()
				.execute('SELECT name,quantity,type,cost  FROM dailySale')]
			for i in self.dailySaleReport.dailySaleData:
				index = self.dailySaleReport.dailySale.InsertStringItem(sys.maxint, i[0])
				self.dailySaleReport.dailySale.SetStringItem(index, 1, str(i[1]))
				self.dailySaleReport.dailySale.SetStringItem(index, 2, i[2])
				self.dailySaleReport.dailySale.SetStringItem(index, 3, str(i[3]))
			self.dailySaleReport.Show()
			self.mainStockReport.Hide()
			self.Layout()

		if (self.mainStockReport.choiceBox.GetString(self.mainStockReport.choiceBox.GetSelection()) =='Main Sales Report'):
			self.mainSaleReport.mainSaleData = [row for row in connection.cur().
				execute('SELECT name,quantity,type,cost,date FROM mainSale')]
			self.mainSaleReport.Show()
			self.mainStockReport.Hide()
			self.Layout()