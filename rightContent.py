#!/user/bin/python
import wx
from salesHandler import SalesHandler, Sales
import datetime


i = datetime.datetime.now()
sale = SalesHandler()
mylist = []
for row in sale.lists():
    mylist.append(row[0])

class updateStock(wx.Panel):
    def __init__(self,parent,id):
        wx.Panel.__init__(self,parent,id)
        self.updateStock()

    def updateStock(self):
        box= wx.GridBagSizer(8,1)
        container = wx.BoxSizer(wx.VERTICAL)

        sizer1 = wx.GridBagSizer(10,3)

        sb = wx.StaticBox(self,-1,'ADD NEW STOCK',size=(500,300))
        boxsizer = wx.StaticBoxSizer(sb, wx.VERTICAL)

        name=wx.StaticText(self,-1,'Name : ')
        self.drinkName = wx.Choice(self,1,choices= mylist,size=(240,35))
        self.drinkName.Bind(wx.EVT_CHOICE,self.onItemSelection)
        sizer1.Add(name,pos=(0,0), flag=wx.EXPAND | wx.ALL, border=2)
        sizer1.Add(self.drinkName,pos=(0,1),flag=wx.EXPAND | wx.ALL, border=2)

        self.check = wx.CheckBox(self,1,'New Drink Name')
        sizer1.Add(self.check,pos=(2,1),flag=wx.EXPAND | wx.LEFT, border=50)
        self.check.Bind(wx.EVT_CHECKBOX, self.onCheck)

        newName = wx.StaticText(self,1,'New Name :')
        self.newPasswordsTextCtrl()
        sizer1.Add(newName,pos=(3,0),flag=wx.EXPAND | wx.ALL, border=2)
        sizer1.Add(self.sizer1, pos=(3,1), flag=wx.EXPAND | wx.ALL, border=2)

        bunch = wx.StaticText(self, 1, 'Quantity :')
        self.quantity = wx.TextCtrl(self, size=(250, 35))
        sizer1.Add(bunch,pos=(4,0),flag=wx.EXPAND | wx.ALL, border=2)
        sizer1.Add(self.quantity, pos=(4, 1), flag=wx.EXPAND | wx.ALL, border=2)

        quantity=wx.StaticText(self,-1,'Purchases : ')
        self.purchase = wx.TextCtrl(self,size=(250,35))
        sizer1.Add(quantity,pos=(5,0), flag=wx.EXPAND | wx.ALL, border=2)
        sizer1.Add(self.purchase,pos=(5,1),flag=wx.EXPAND | wx.ALL, border=2)

        cost = wx.StaticText(self, -1, 'Sales : ')
        self.sale = wx.TextCtrl(self, size=(250, 35))
        sizer1.Add(cost, pos=(6, 0), flag=wx.EXPAND | wx.ALL, border=2)
        sizer1.Add(self.sale, pos=(6, 1), flag=wx.EXPAND | wx.ALL, border=2)

        date=wx.StaticText(self,-1,'Date : ')
        value = '{day}/{month}/{year}'.format(day=i.day, month=i.month, year=i.year)
        self.drinkDate = wx.TextCtrl(self,size=(250,30), value=value)

        sizer1.Add(date,pos=(7,0), flag=wx.EXPAND | wx.LEFT, border=30)
        sizer1.Add(self.drinkDate,pos=(7,1),flag=wx.EXPAND | wx.ALL, border=2)

        self.updateStatus=wx.StaticText(self,-1,' ')
        sizer1.Add(self.updateStatus,pos=(10,1), flag=wx.EXPAND | wx.ALL, border=2)

        self.btnSaveDrink = wx.Button(self,1,'Save',size=(150,40))
        self.btnSaveDrink.Bind(wx.EVT_BUTTON, self.onAddButton)
        sizer1.Add(self.btnSaveDrink,pos=(8,2),flag=wx.EXPAND | wx.ALL, border=2)

        box.Add(sizer1,pos=(0,0),flag=wx.EXPAND | wx.ALL, border=5)

        boxsizer.Add(box, flag=wx.EXPAND | wx.TOP,border=50)
        container.Add(boxsizer, wx.EXPAND | wx.TOP,border=50)

        self.SetSizer(container)
        self.checked = False

    def onAddButton(self):
        index = self.drinkName.GetStringSelection
        quantity = self.quantity.GetValue()
        purchase = self.purchase.GetValue()
        date = self.drinkDate.GetValue()
        sale = self.sale.GetValue()

        if index != -1:
            try:
                int(quantity)
                int(purchase)
                int(sale)
                if self.checked:
                        saler = Sales(self.text_no_password1.GetValue(), quantity )
                        saler.connect.cur().execute("INSERT INTO mainStock (name,quantity,saleCost,purCost,date) "
                                                    "VALUES('{name}',{amount},{saleCost},{purCost},'{date}')"
                                                    .format(name=saler.getName(), amount=saler.getAmount(),
                                                            saleCost=sale, purCost=purchase, date=date))
                        saler.connect.cur().execute("INSERT INTO dailySale (name, quantity, sales, profit, date) VALUES('{name}',0,0,0,'{date}')"
                                                    .format(name=saler.getName(), date= date))
                        saler.connect.commit()
                        self.updateStatus.SetLabel('Data saved')
                        self.quantity.SetValue('')
                        self.purchase.SetValue('')
                        self.drinkDate.SetValue('')
                        self.sale.SetValue('')
                        self.text_no_password1.SetValue('')
                        self.updateStatus.SetLabel('Data saved')
                else:
                    name = self.drinkName.GetString(self.drinkName.GetSelection())
                    saler = Sales(name, quantity)
                    saler.connect.cur().execute("UPDATE mainStock SET quantity = (SELECT quantity FROM mainStock WHERE name = '{name}') +"
                                                " {amount}, date = '{date}' , saleCost = '{sales}', purCost ='{purCost}'  WHERE name = '{name}'"
                                                .format(name=saler.getName(), amount=saler.getAmount(),date=date, purCost = purchase, sales =sale))
                    saler.connect.commit()
                    self.quantity.SetValue('')
                    self.purchase.SetValue('')
                    self.drinkDate.SetValue('')
                    self.sale.SetValue('')
                    self.updateStatus.SetLabel('Data saved')
            except ValueError:
                wx.MessageBox('Wrong value on Quantity')

    def onItemSelection(self, eve):
        self.updateStatus.SetLabel('')



    def newPasswordsTextCtrl(self):
        self.password_shown1 = False
        self.sizer1 = wx.BoxSizer(wx.HORIZONTAL)
        self.text_password1 = wx.TextCtrl(self, style=wx.TE_READONLY, size=(240,35))
        self.sizer1.Add(self.text_password1, 0, wx.ALL, 0)
        self.text_no_password1 = wx.TextCtrl(self, size=(240,35))
        self.text_no_password1.Hide()
        self.sizer1.Add(self.text_no_password1, 0, wx.ALL, 0)


    def onCheck(self, event):
        self.checked = not self.checked
        self.text_password1.Show(self.password_shown1)
        self.text_no_password1.Show(not self.password_shown1)
        if not self.password_shown1:
            self.text_no_password1.SetValue(self.text_password1.GetValue())
            self.text_no_password1.SetFocus()
        else:
            self.text_password1.SetValue('')
            self.text_password1.SetFocus()
        self.text_password1.GetParent().Layout()
        self.password_shown1 = not self.password_shown1

class editStock(wx.Panel):
    def __init__(self,parent,id):
        wx.Panel.__init__(self, parent,id)

        self.editStock()

    def populate(self):
        mylist = []
        for row in sale.lists():
            mylist.append(row[0])
        self.drinkNameEdit.SetItems(mylist)

    def editStock(self):
        box= wx.wx.GridBagSizer(8,1)
        container = wx.BoxSizer(wx.VERTICAL)

        sizer1 = wx.GridBagSizer(5,4)

        sb = wx.StaticBox(self, -1, 'EDIT STOCK',size=(500,900))
        boxsizer = wx.StaticBoxSizer(sb, wx.VERTICAL)

        name=wx.StaticText(self,-1,'Name : ')
        self.drinkNameEdit = wx.Choice(self,1,size=(240,30))
        self.populate()
        self.drinkNameEdit.Bind(wx.EVT_CHOICE, self.onItemSelection)
        sizer1.Add(name,pos=(0,0), flag=wx.EXPAND | wx.ALL, border=2)
        sizer1.Add(self.drinkNameEdit,pos=(0,1),flag=wx.EXPAND | wx.ALL, border=5)

        quantity=wx.StaticText(self,-1,'Quantity : ')
        self.drinkQuantityEdit = wx.TextCtrl(self,size=(250,30))
        sizer1.Add(quantity,pos=(1,0), flag=wx.EXPAND | wx.ALL, border=2)
        sizer1.Add(self.drinkQuantityEdit,pos=(1,1),flag=wx.EXPAND | wx.ALL, border=5)

        cost = wx.StaticText(self, -1, 'Purchase : ')
        self.costText = wx.TextCtrl(self, size=(250, 30))
        sizer1.Add(cost, pos=(2, 0), flag=wx.EXPAND | wx.ALL, border=2)
        sizer1.Add(self.costText, pos=(2, 1), flag=wx.EXPAND | wx.ALL, border=5)

        salestatic = wx.StaticText(self, -1, 'Sales : ')
        self.salesText = wx.TextCtrl(self, size=(250, 30))
        sizer1.Add(salestatic, pos=(3, 0), flag=wx.EXPAND | wx.ALL, border=2)
        sizer1.Add(self.salesText, pos=(3, 1), flag=wx.EXPAND | wx.ALL, border=5)

        self.editStatus=wx.StaticText(self,-1,' ')
        sizer1.Add(self.editStatus,pos=(4,1), flag=wx.EXPAND | wx.ALL, border=2)

        self.btnEditDrink = wx.Button(self,1,'Save',size=(150,40))
        sizer1.Add(self.btnEditDrink,pos=(5,2),flag=wx.EXPAND | wx.ALL, border=2)
        self.Bind(wx.EVT_BUTTON, self.onSelectSave)

        box.Add(sizer1,pos=(0,0),flag=wx.EXPAND | wx.ALL, border=5)

        boxsizer.Add(box, flag=wx.EXPAND | wx.LEFT,border=5)
        container.Add(boxsizer, wx.EXPAND | wx.TOP,border=50)

        self.SetSizer(container)

    def onItemSelection(self, eve):
        self.editStatus.SetLabel('')

    def saveChanges(self, label):
        self.editStatus.SetLabel(label)
        self.drinkQuantityEdit.SetValue('')
        self.costText.SetValue('')
        self.salesText.SetValue('')

    def onSelectSave(self, event):
        index = self.drinkNameEdit.GetSelection()
        if index != -1:
            name = self.drinkNameEdit.GetString(index)
            amount = self.drinkQuantityEdit.GetValue()
            cost = self.costText.GetValue()
            salingCost = self.salesText.GetValue()
            try:
                if amount:
                    int(amount)
                    if cost:
                        int(cost)
                        if salingCost:
                            # salingcost, purchaseCost and amount updated
                            int(salingCost)
                            sale.connect.cur().execute(
                                "UPDATE mainStock SET quantity = {amount}, saleCost = {salingCost}, purCost = {cost} WHERE name ='{name}'"
                                    .format(name=name, amount=amount, cost=cost, salingCost=salingCost))
                            sale.connect.commit()
                            self.saveChanges('Data Saved')
                        else:
                            # Quantity and purchase cost updates
                            sale.connect.cur().execute("UPDATE mainStock SET quantity = {amount}, purCost = {cost} WHERE name ='{name}'"
                                                   .format(name=name, amount=amount, cost=cost ))
                            sale.connect.commit()
                            self.saveChanges('Quantity and Purchase cost Edited')
                    elif salingCost:
                        # quantity and sailing cost updated
                        int(salingCost)
                        sale.connect.cur().execute(
                            "UPDATE mainStock SET quantity = {amount}, saleCost = {salingCost} WHERE name ='{name}'"
                                .format(name=name, amount=amount, salingCost=salingCost))
                        sale.connect.commit()
                        self.saveChanges('Quantity and Sales cost Edited')
                    else:
                        # Quantity only edited
                        sale.connect.cur().execute(
                            "UPDATE mainStock SET quantity = {amount} WHERE name ='{name}'"
                            .format(name=name, amount=amount))
                        sale.connect.commit()
                        self.saveChanges('Quantity Edited')
                elif cost:
                    int(cost)
                    if salingCost:
                        # Saling cost and purchase cost update
                        int(cost)
                        sale.connect.cur().execute("UPDATE mainStock SET saleCost = {salingCost}, purCost = {cost} WHERE name ='{name}'"
                                               .format(name=name, cost=cost, salingCost=salingCost ))
                        sale.connect.commit()
                        self.saveChanges('Sales prices and purchases price edited')
                    else:
                        # purchase cost only update
                        sale.connect.cur().execute(
                            "UPDATE mainStock SET purCost = {cost} WHERE name ='{name}'"
                            .format(name=name, cost=cost))
                        sale.connect.commit()
                        self.saveChanges('Cost Edited')
                elif salingCost:
                    int(salingCost)
                    # sales cost only update
                    sale.connect.cur().execute(
                        "UPDATE mainStock SET saleCost = {salingCost} WHERE name ='{name}'"
                            .format(name=name, salingCost=salingCost))
                    sale.connect.commit()
                    self.saveChanges('Sales Cost changed')
                else:
                    # no information filled at all
                    wx.MessageBox("Fill in correct information")
            except ValueError:
                wx.MessageBox('Enter the correct data please', 'Info')
        else: wx.MessageBox('Please choose a drink name', 'Error')


    def onChoice(self, event):
        self.drinkQuantityEdit.SetValue('')


class Content1(wx.Panel):
    def __init__(self, parent, id):
        wx.Panel.__init__(self, parent,id)
        box= wx.GridBagSizer(3,1)

        self.editStock = editStock(self,-1)
        self.updateStock = updateStock(self,-1)
        self.updateStock.btnSaveDrink.Bind(wx.EVT_BUTTON, self.onAddButton)
        box.Add(self.updateStock,pos=(0,0),flag=wx.EXPAND | wx.LEFT | wx.TOP,border=20)
        box.Add(self.editStock,pos=(0,2),flag=wx.EXPAND | wx.LEFT | wx.TOP,border=20)
        self.SetSizer(box)
        self.Show()

    def onAddButton(self,event):
        self.updateStock.onAddButton()
        self.editStock.populate()
