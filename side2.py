import wx
import sys
from wx.lib.mixins.listctrl import CheckListCtrlMixin, ListCtrlAutoWidthMixin
from salesHandler import SalesHandler
from salesHandler import Sales
import datetime
from databaseConn import DatabaseConn
connection = DatabaseConn()

sale = SalesHandler()
mylist = []
for row in sale.lists():
    mylist.append(row[0])
date = datetime.datetime.now()
vdate = '{day}/{month}/{year}'.format(day=date.day, month=date.month, year=date.year)
from saleController import leftContent,rightContent


class salew(wx.Panel):
	def __init__(self, parent,id):
		super(salew, self).__init__(parent, id)
		self.InUI()
		self.Fit()
		self.Show()

	def InUI(self):
		self.index = -1
		box = wx.GridBagSizer(2,2)
		txt = wx.StaticText(self, -1, 'Drinks Management System')

		stline = wx.StaticLine(self)
		box.Add(txt, pos=(0, 1), flag=wx.EXPAND | wx.TOP, border=3)
		box.Add(stline, pos=(1, 0), span=(1, 5), flag=wx.EXPAND | wx.BOTTOM, border=0)

		self.left = leftContent(self,-1)
		self.right = rightContent(self,-1)
		self.left.list.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnSelectItem)
		self.right.qInx.Bind(wx.EVT_BUTTON, self.AddButton)
		self.right.qDx.Bind(wx.EVT_BUTTON, self.SubButton)
		self.right.btnClear.Bind(wx.EVT_BUTTON, self.OnSeleClear)
		self.right.btnOksession.Bind(wx.EVT_BUTTON, self.OnSeleOkButton)
		self.right.okButton.Bind(wx.EVT_BUTTON, self.onSaveSession)
		self.right.btnSession.Bind(wx.EVT_BUTTON, self.editSession)
		self.right.sessionText.Bind(wx.EVT_KEY_UP, self.enterkey)
		self.right.btnSession.Bind(wx.EVT_KEY_UP, self.enterkey)
		self.right.quantityStatus.Bind(wx.EVT_LIST_ITEM_SELECTED,self.onclear)
		box.Add(self.left,pos=(2,0),flag=wx.EXPAND |
			wx.ALL,border=5)
		box.Add(self.right,pos=(2,2),flag=wx.EXPAND |
			wx.ALL,border=5)
		self.SetSizer(box)
		self.session = 1
		self.notInSession = True
		self.lastSession = 0
		self.quantOrdertot=0
		self.costOrdertot = 0

	def enterkey(self, event):
		keycode = event.GetKeyCode()
		if keycode == wx.WXK_RETURN or keycode == wx.WXK_NUMPAD_ENTER:
			self.editSession(event=None)
			event.EventObject.Navigate()
		event.Skip()

	def OnSelectItem(self, event):
		self.right.setZero()

	def AddButton(self, event):
		value = self.right.textQuantity.GetValue()
		if value:
			newValue = int(value)
			if newValue >= 0:
				newValue += 1
				self.right.textQuantity.SetValue(str(newValue))
			else:
				self.right.textQuantity.SetValue('0')
		else:
			self.right.textQuantity.SetValue('1')

	def SubButton(self, event):
		value = self.right.textQuantity.GetValue()
		if value:
			newValue = int(value)
			if newValue > 0:
				newValue -= 1
				self.right.textQuantity.SetValue(str(newValue))
			else:
				self.right.textQuantity.SetValue('0')
		else:
			self.right.textQuantity.SetValue('1')

	def OnSeleOkButton(self, event):
		index = self.left.list.GetFirstSelected()
		try:
			if int(self.right.textQuantity.GetValue()) != 0:
				if index != -1:
					self.quantOrdertot = int(self.right.textQuantity.GetValue())+self.quantOrdertot
					self.sale = Sales(self.left.list.GetItemText(index),
									  self.right.textQuantity.GetValue())
					self.right.Data.append(
						(self.sale.getName(), self.sale.getAmount(), self.sale.getTotalCost()))
					self.costOrdertot = int(self.sale.getTotalCost())+self.costOrdertot
					self.right.quantityStatus.DeleteItem(self.right.quantityStatus.GetItemCount()-1)
					for i in self.right.Data:
						index = self.right.quantityStatus.InsertStringItem(sys.maxint, i[0])
						self.right.quantityStatus.SetStringItem(index, 1, i[1])
						self.right.quantityStatus.SetStringItem(index, 2, i[2])
					self.right.Data = []
					index = self.right.quantityStatus.InsertStringItem(sys.maxint, "Total")
					self.right.quantityStatus.SetStringItem(index, 1,str(self.quantOrdertot))
					self.right.quantityStatus.SetStringItem(index, 2, str(self.costOrdertot))
					self.right.valueData.append((self.sale.getName(), self.sale.getAmount(), self.sale.getTotalCost()))
					self.right.textQuantity.SetValue('1')
				else:
					wx.MessageBox('Please select a drink', 'Error')
			else:
				wx.MessageBox('Enter Quantity Please')

		except ValueError:
			wx.MessageBox('Wrong Amount')
	# Saving the order to the database (This is down ok button event method)
	def onSaveSession(self, e):
		if self.right.valueData:
			if self.notInSession:
				# we are here because we are trying to enter new orders
				for row in self.right.valueData:
					# inserting the new order to the orders table
					sale.connect.cur().execute("INSERT INTO session(sNo, name, quantity, cost, date) VALUES ({sNo}, "
											   "'{name}', {quantity}, {cost}, '{date}')"
											   .format(sNo=self.session, name=row[0], quantity=row[1], cost=row[2],
													   date=vdate))
					# updating the dailySale table quantity and sales values
					sale.connect.cur().execute("UPDATE dailySale SET quantity = (SELECT quantity FROM dailySale WHERE "
											   "name = '{name}')+{quantity}, sales = (SELECT sales FROM dailySale  WHERE "
											   "name = '{name}')+{cost}, date = '{date}' WHERE name = '{name}'"
											   .format(name=row[0], quantity=row[1], cost=row[2], date=vdate))
					# calculatin and changing the value of profit
					sale.connect.cur().execute("UPDATE dailySale SET profit = (SELECT sales FROM dailySale WHERE name ='{name}')-"
											   "(SELECT purCost FROM mainStock WHERE name = '{name}')*(SELECT quantity FROM dailySale "
											   "WHERE name = '{name}') where name = '{name}'".format(name=row[0]))
				sale.connect.commit()
				self.quantOrdertot = 0
				self.costOrdertot = 0
				self.session = self.session + 1
				self.right.sessionNo.SetLabel('Order No: ' + str(self.session))
				self.right.quantityStatus.DeleteAllItems()
				self.right.Data = []
				self.right.valueData = []
			else:
				# we are here because we are changing the value(s) of a order
				# remove the past records of the order
				for i in self.pastSessionData:
					# decreasing the daily sales
					sale.connect.cur().execute("UPDATE dailySale SET quantity = (SELECT quantity  FROM dailySale WHERE "
											 "name = '{name}') - {quantity} , sales =(SELECT sales  FROM dailySale WHERE "
											 "name = '{name}')-{cost} WHERE name = '{name}'"
											 .format(name=i[0], quantity=i[1], cost=i[2]))
					# removing the records from the session/orders table
				sale.connect.cur().execute('DELETE FROM session WHERE sNo={sno}'.format(sno=self.orderNo))
				# placing back the good edited data
				for row in self.right.valueData:
					#inserting the edited data into the  database file
					sale.connect.cur().execute("INSERT INTO session(sNo, name, quantity, cost, date) VALUES ({sNo}, "
											   "'{name}', {quantity}, {cost}, '{date}')"
											   .format(sNo=self.orderNo, name=row[0], quantity=row[1], cost=row[2],
													   date=vdate))\
					#updating the daily sales
					sale.connect.cur().execute("UPDATE dailySale SET quantity = (SELECT quantity FROM dailySale WHERE "
											   "name = '{name}')+{quantity}, sales = (SELECT sales FROM dailySale  WHERE "
											   "name = '{name}')+{cost} WHERE name = '{name}'"
											   .format(name=row[0], quantity=row[1], cost=row[2]))
				sale.connect.commit()
				self.right.sessionNo.SetLabel('Order No: ' + str(self.session))
				self.right.quantityStatus.DeleteAllItems()
				self.right.Data = []
				self.right.valueData = []
				self.notInSession = True
		else:
			wx.MessageBox('No orders entered', 'INFO')

	def editSession(self, event):
		try:
			print
			self.orderNo = int(self.right.sessionText.GetValue())
			ipo = False
			self.notInSession = False
			sessionAva = [numbers for numbers in connection.cur().execute('SELECT DISTINCT(sNo) FROM session;')]
			for row in sessionAva:
				if (int(row[0]) == self.orderNo):
					ipo = True
					break
			if ipo:
				if self.right.quantityStatus.GetItemCount() == 0:
					data = [row for row in
							connection.cur().execute('SELECT  name,quantity,cost  FROM session WHERE sNo={sno}'
													 .format(sno=self.orderNo))]
					self.right.valueData = data
					self.pastSessionData = data
					self.quantOrdertot = 0
					self.costOrdertot = 0
					for i in data:
						index = self.right.quantityStatus.InsertStringItem(sys.maxint, i[0])
						self.costOrdertot = self.costOrdertot + int(i[2])
						self.quantOrdertot = self.quantOrdertot + int(i[1])
						self.right.quantityStatus.SetStringItem(index, 1, str(i[1]))
						self.right.quantityStatus.SetStringItem(index, 2, str(i[2]))
					self.right.sessionNo.SetLabel('Order No: ' + str(self.orderNo))
					index = self.right.quantityStatus.InsertStringItem(sys.maxint, "Total")
					self.right.quantityStatus.SetStringItem(index, 1, str(self.quantOrdertot))
					self.right.quantityStatus.SetStringItem(index, 2, str(self.costOrdertot))
					self.right.sessionText.SetValue('')
				else:
					wx.MessageBox("Please save the previous order first")
			else:
				wx.MessageBox("No such order number in our database")
		except ValueError:
			wx.MessageBox('Enter a correct order number')



	def onclear(self, e):
		self.index = e.GetIndex()

	def OnSeleClear(self, event):
		if self.index != -1:
			if self.index != self.right.quantityStatus.GetItemCount()-1:
				self.quantOrdertot = self.quantOrdertot - int(self.right.quantityStatus.GetItemText(self.index, col=1))
				self.costOrdertot = self.costOrdertot - int(self.right.quantityStatus.GetItemText(self.index, col=2))
				self.right.quantityStatus.DeleteItem(self.right.quantityStatus.GetItemCount() - 1)
				index = self.right.quantityStatus.InsertStringItem(sys.maxint, "Total")
				self.right.quantityStatus.SetStringItem(index, 1, str(self.quantOrdertot))
				self.right.quantityStatus.SetStringItem(index, 2, str(self.costOrdertot))
				self.right.quantityStatus.DeleteItem(self.index)
				self.right.valueData.pop(self.index)
				self.index = -1
			else:
				wx.MessageBox('You cannot delete the Total row', 'Info')
		else:
			wx.MessageBox('Please Select Row to Delete', 'Info')
