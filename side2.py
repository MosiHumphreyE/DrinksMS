import sys
import wx
dailySaleData = [('Tendulkar', '15000', '100'), ('Dravid', '14000', '1'),
('Kumble', '1000', '700'), ('KapilDev', '5000', '400'),
('Ganguly', '8000', '50')]

mainSaleData = [('Tendulkar', '15000', '100'), ('Dravid', '14000', '1'),
('Kumble', '1000', '700'), ('KapilDev', '5000', '400'),
('Ganguly', '8000', '50')]

mainStockData = [('Tendulkar', '15000', '100'), ('Dravid', '14000', '1'),
('Kumble', '1000', '700'), ('KapilDev', '5000', '400'),
('Ganguly', '8000', '50')]

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
		self.btnShow = wx.Button(self,1,'Show',size=(150,35))
		self.hbUp.Add(self.btnShow, wx.EXPAND,border = 5)
		st1= wx.StaticText(self,1,'')
		self.hbUp.Add(st1, wx.EXPAND,border = 5)

		self.dailySale = wx.ListCtrl(self, -1, style=wx.LC_REPORT)
		self.dailySale.InsertColumn(0, 'Name', width=200)
		self.dailySale.InsertColumn(1, 'Quantity', wx.LIST_FORMAT_RIGHT, 200)
		self.dailySale.InsertColumn(2, 'Type', wx.LIST_FORMAT_RIGHT, 200)
		self.dailySale.InsertColumn(3, 'Cost', wx.LIST_FORMAT_RIGHT, 200)

		for i in dailySaleData:
		 	index = self.dailySale.InsertStringItem(sys.maxint, i[0])
		 	self.dailySale.SetStringItem(index, 1, i[1])
			self.dailySale.SetStringItem(index, 2, i[2])
		box.Add(self.dailySale,flag=wx.EXPAND | wx.ALL,border=5)

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
		self.btnShow = wx.Button(self,1,'Show',size=(150,35))
		self.hbUp.Add(self.btnShow, wx.EXPAND,border = 5)
		st1= wx.StaticText(self,1,'')
		self.hbUp.Add(st1, wx.EXPAND,border = 5)
		st2= wx.StaticText(self,1,'')
		self.hbUp.Add(st2, wx.EXPAND,border = 5)

		self.mainSale = wx.ListCtrl(self,-1,style=wx.LC_REPORT)
		self.mainSale.InsertColumn(0, 'Name', width=200)
		self.mainSale.InsertColumn(1, 'Quantity', wx.LIST_FORMAT_RIGHT, 200)
		self.mainSale.InsertColumn(2, 'Type', wx.LIST_FORMAT_RIGHT, 200)
		self.mainSale.InsertColumn(3, 'Cost', wx.LIST_FORMAT_RIGHT, 200)
		self.mainSale.InsertColumn(4, 'Date', wx.LIST_FORMAT_RIGHT, 200)

		for i in mainSaleData:
		 	index = self.mainSale.InsertStringItem(sys.maxint, i[0])
		 	self.mainSale.SetStringItem(index, 1, i[1])
		 	self.mainSale.SetStringItem(index, 2, i[2])
		box.Add(self.mainSale,flag=wx.EXPAND | wx.ALL,border=5)

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
		self.btnShow = wx.Button(self, 1, 'Show', size=(150, 35))
		self.hbUp.Add(self.btnShow, wx.EXPAND, border=5)
		st1= wx.StaticText(self,1,'')
		self.hbUp.Add(st1, wx.EXPAND,border = 5)
		st2= wx.StaticText(self,1,'')
		self.hbUp.Add(st2, wx.EXPAND,border = 5)

		self.mainStock = wx.ListCtrl(self,-1,style=wx.LC_REPORT)
		self.mainStock.InsertColumn(0, 'Name', width=200)
		self.mainStock.InsertColumn(1, 'Quantity', wx.LIST_FORMAT_RIGHT, 200)
		self.mainStock.InsertColumn(2, 'Type', wx.LIST_FORMAT_RIGHT, 200)
		self.mainStock.InsertColumn(3, 'Cost@Drink', wx.LIST_FORMAT_RIGHT, 200)
		self.mainStock.InsertColumn(4, 'Date', wx.LIST_FORMAT_RIGHT, 200)
		box.Add(self.mainStock,flag=wx.EXPAND | wx.ALL,border=5)

		for i in mainStockData:
			index = self.mainStock.InsertStringItem(sys.maxint, i[0])
		 	self.mainStock.SetStringItem(index, 1, i[1])
			self.mainStock.SetStringItem(index, 2, i[2])
		sizer.Add(self.hbUp,pos=(0,0),flag=wx.EXPAND | wx.ALL,border=5)
		sizer.Add(box,pos=(2,0),flag=wx.EXPAND | wx.ALL,border=5)
		self.SetSizer(sizer)
		self.Fit()
		self.Show(True)

class Mywin(wx.Frame):
	def __init__(self, parent, id,title):
		super(Mywin, self).__init__(parent, id,title=title)
		panel=wx.Panel(self)
		self.hbDown = wx.BoxSizer()

		self.dailySaleReport = dailySaleReport(panel,-1)
		self.mainSaleReport = mainSaleReport(panel,-1)
		self.mainStockReport = mainStockReport(panel,-1)

		self.hbDown.Add(self.dailySaleReport,1, flag=wx.EXPAND | wx.ALL, border=5)
		self.hbDown.Add(self.mainSaleReport, 1,flag=wx.EXPAND | wx.ALL, border=5)
		self.hbDown.Add(self.mainStockReport,1, flag=wx.EXPAND | wx.ALL, border=5)

		self.mainSaleReport.Hide()
		self.mainStockReport.Hide()
		self.dailySaleReport.btnShow.Bind(wx.EVT_BUTTON,self.OnClick)
		self.mainSaleReport.btnShow.Bind(wx.EVT_BUTTON,self.OnClick1)
		self.mainStockReport.btnShow.Bind(wx.EVT_BUTTON,self.OnClick2)
		panel.SetSizer(self.hbDown)
		self.Centre()
		self.Show(True)

	def OnClick(self,evt):
		if (self.dailySaleReport.choiceBox.GetString(self.dailySaleReport.choiceBox.GetSelection()) =='Main Sales Report'):
			self.mainSaleReport.Show()
			self.dailySaleReport.Hide()
			self.Layout()

		if (self.dailySaleReport.choiceBox.GetString(self.dailySaleReport.choiceBox.GetSelection()) =='Main Stock Report'):
			self.mainStockReport.Show()
			self.dailySaleReport.Hide()
			#self.Layout()

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

ex = wx.App()
Mywin(None,-1,'ListCtrl Demo')
ex.MainLoop()