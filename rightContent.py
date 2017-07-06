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

        list=['Alcohol Drinks','Soft Drinks']
        self.choiceDrink = wx.RadioBox(self, label= 'Drink Type',size=(250,50),choices=list)
        sizer1.Add(self.choiceDrink,pos=(5,1),flag=wx.EXPAND | wx.LEFT, border=5)

        quantity=wx.StaticText(self,-1,'Quantity : ')
        self.drinkQuantity = wx.TextCtrl(self,size=(250,35))
        sizer1.Add(quantity,pos=(6,0), flag=wx.EXPAND | wx.ALL, border=2)
        sizer1.Add(self.drinkQuantity,pos=(6,1),flag=wx.EXPAND | wx.ALL, border=2)

        cost = wx.StaticText(self, -1, 'Cost/Drink : ')
        self.costte = wx.TextCtrl(self, size=(250, 35))
        sizer1.Add(cost, pos=(7, 0), flag=wx.EXPAND | wx.ALL, border=2)
        sizer1.Add(self.costte, pos=(7, 1), flag=wx.EXPAND | wx.ALL, border=2)

        date=wx.StaticText(self,-1,'Date : ')
        value = '{day}/{month}/{year}'.format(day=i.day, month=i.month, year=i.year)
        self.drinkDate = wx.TextCtrl(self,size=(250,30), value=value)

        sizer1.Add(date,pos=(8,0), flag=wx.EXPAND | wx.LEFT, border=30)
        sizer1.Add(self.drinkDate,pos=(8,1),flag=wx.EXPAND | wx.ALL, border=2)

        self.updateStatus=wx.StaticText(self,-1,' ')
        sizer1.Add(self.updateStatus,pos=(10,1), flag=wx.EXPAND | wx.ALL, border=2)

        self.btnSaveDrink = wx.Button(self,1,'Save',size=(150,40))
        self.btnSaveDrink.Bind(wx.EVT_BUTTON, self.onAddButton)
        sizer1.Add(self.btnSaveDrink,pos=(9,2),flag=wx.EXPAND | wx.ALL, border=2)

        box.Add(sizer1,pos=(0,0),flag=wx.EXPAND | wx.ALL, border=5)

        boxsizer.Add(box, flag=wx.EXPAND | wx.TOP,border=50)
        container.Add(boxsizer, wx.EXPAND | wx.TOP,border=50)

        self.SetSizer(container)
        self.checked = False

    def onAddButton(self, event):
        index = self.drinkName.GetStringSelection
        cost = self.costte.GetValue()
        date = self.drinkDate.GetValue()

        if index != -1:
            try:
                float(self.drinkQuantity.GetValue())
                self.type = ''
                if self.choiceDrink.GetStringSelection() == 'Alcohol Drinks':
                    self.type = 'Alcohol'
                else:
                    self.type = 'Soft Drinks'
                if self.checked:
                    try:
                        int(self.costte.GetValue())
                        saler = Sales(self.text_no_password1.GetValue(), self.drinkQuantity.GetValue())
                        saler.connect.cur().execute("INSERT INTO mainStock (name,quantity,type,costperdrink,date) "
                                                    "VALUES('{name}',{amount},'{type}',{cost},'{date}')"
                                                    .format(name=saler.getName(), amount=saler.getAmount(),
                                                            type=self.type
                                                            , cost=cost, date=date))
                        saler.connect.commit()
                        self.updateStatus.SetLabel('Data saved')
                        self.drinkQuantity.SetValue('')
                        self.costte.SetValue('')
                        self.text_no_password1.SetValue('')
                    except ValueError:
                        wx.MessageBox('Wrong value Cost/Drink')
                else:
                    name = self.drinkName.GetString(self.drinkName.GetSelection())
                    saler = Sales(name, self.drinkQuantity.GetValue())
                    saler.connect.cur().execute("UPDATE mainStock SET quantity = (SELECT quantity FROM mainStock WHERE name = '{name}') + {amount}, date = '{date}' WHERE name = '{name}'".format(name=saler.getName(), amount=saler.getAmount(),
                                                                    date=date))
                    saler.connect.commit()
                    self.drinkQuantity.SetValue('')
                    self.costte.SetValue('')
                    self.updateStatus.SetLabel('Data saved')

            except ValueError:
                wx.MessageBox('Wrong value Quantity')

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

    def editStock(self):
        box= wx.wx.GridBagSizer(8,1)
        container = wx.BoxSizer(wx.VERTICAL)

        sizer1 = wx.GridBagSizer(4,4)

        sb = wx.StaticBox(self, -1, 'EDIT STOCK',size=(500,900))
        boxsizer = wx.StaticBoxSizer(sb, wx.VERTICAL)

        name=wx.StaticText(self,-1,'Name : ')
        self.drinkNameEdit = wx.Choice(self,1,choices=mylist,size=(240,30))
        self.drinkNameEdit.Bind(wx.EVT_CHOICE, self.onItemSelection)
        sizer1.Add(name,pos=(0,0), flag=wx.EXPAND | wx.ALL, border=2)
        sizer1.Add(self.drinkNameEdit,pos=(0,1),flag=wx.EXPAND | wx.ALL, border=5)

        quantity=wx.StaticText(self,-1,'Quantity : ')
        self.drinkQuantityEdit = wx.TextCtrl(self,size=(250,30))
        sizer1.Add(quantity,pos=(1,0), flag=wx.EXPAND | wx.ALL, border=2)
        sizer1.Add(self.drinkQuantityEdit,pos=(1,1),flag=wx.EXPAND | wx.ALL, border=5)

        cost = wx.StaticText(self, -1, 'Cost/Drink : ')
        self.costText = wx.TextCtrl(self, size=(250, 30))
        sizer1.Add(cost, pos=(2, 0), flag=wx.EXPAND | wx.ALL, border=2)
        sizer1.Add(self.costText, pos=(2, 1), flag=wx.EXPAND | wx.ALL, border=5)

        self.editStatus=wx.StaticText(self,-1,' ')
        sizer1.Add(self.editStatus,pos=(3,1), flag=wx.EXPAND | wx.ALL, border=2)

        self.btnEditDrink = wx.Button(self,1,'Save',size=(150,40))
        sizer1.Add(self.btnEditDrink,pos=(4,2),flag=wx.EXPAND | wx.ALL, border=2)
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

    def onSelectSave(self, event):
        name = self.drinkNameEdit.GetString(self.drinkNameEdit.GetSelection())
        amount = self.drinkQuantityEdit.GetValue()
        cost = self.costText.GetValue()
        try:
            if amount:
                if cost:
                    float(amount)
                    int(cost)
                    sale.connect.cur().execute(
                        "UPDATE mainStock SET quantity = {amount}, costperdrink = {cost} WHERE name ='{name}'"
                        .format(name=name, amount=amount, cost=cost))
                    sale.connect.commit()
                    self.saveChanges('Quantity & Cost/Drink Edited')
                else:
                    float(amount)
                    sale.connect.cur().execute("UPDATE mainStock SET quantity = {amount} WHERE name ='{name}'"
                                               .format(name=name, amount=amount, ))
                    sale.connect.commit()
                    self.saveChanges('Quantity Edited')

            elif cost:
                int(cost)
                sale.connect.cur().execute("UPDATE mainStock SET costperdrink = {cost} WHERE name ='{name}'"
                    .format(name=name, cost=cost, ))
                sale.connect.commit()
                self.saveChanges('Cost Edited')
            else:
                wx.MessageBox('Drink Quantity OR Cost/Drink not filled', 'Info')
        except ValueError:
            wx.MessageBox('Enter the correct amount OR Cost/Drink', 'Info')


    def onChoice(self, event):
        self.drinkQuantityEdit.SetValue('')


class Content1(wx.Panel):
    def __init__(self, parent, id):
        wx.Panel.__init__(self, parent,id)
        box= wx.GridBagSizer(3,1)

        self.editStock = editStock(self,-1)
        self.updateStock = updateStock(self,-1)
        box.Add(self.updateStock,pos=(0,0),flag=wx.EXPAND | wx.LEFT | wx.TOP,border=20)
        box.Add(self.editStock,pos=(0,2),flag=wx.EXPAND | wx.LEFT | wx.TOP,border=20)
        self.SetSizer(box)
        self.Show()