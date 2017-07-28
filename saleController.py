#!/user/bin/python
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

class CheckListCtrl(wx.ListCtrl, CheckListCtrlMixin, ListCtrlAutoWidthMixin):
    def __init__(self, parent):
        wx.ListCtrl.__init__(self, parent, -1, style=wx.LC_REPORT | wx.SUNKEN_BORDER,size=(200,550))
        CheckListCtrlMixin.__init__(self)
        ListCtrlAutoWidthMixin.__init__(self)


class rightContent(wx.Panel):
    def __init__(self,parent,id):
        wx.Panel.__init__(self,parent,id)
        self.sizer = wx.GridBagSizer(5,5)
        sizer1 = wx.GridBagSizer(5,5)
        sizer2 = wx.GridBagSizer(5,5)
        sizer3 = wx.GridBagSizer(7,7)
        sizer4 = wx.GridBagSizer(2, 2)
        txt1 = wx.StaticText(self,-1,'Quantity')
        self.textQuantity = wx.TextCtrl(self)
        self.qInx = wx.Button(self,-1,'+')
        self.qDx = wx.Button(self,-1,'-')
        self.quantityStatus = wx.ListCtrl(self, -1, size=(605, 400), style=wx.LB_SINGLE|wx.LC_VRULES|wx.LC_HRULES)
        self.quantityStatus.InsertColumn(0, 'Name', width=200)
        self.quantityStatus.InsertColumn(1, 'Quantity', wx.LIST_FORMAT_RIGHT, 200)
        self.quantityStatus.InsertColumn(2, 'Cost', wx.LIST_FORMAT_RIGHT, 200)
        self.Data = []
        self.valueData = []
        self.okButton = wx.Button(self,-1,'OK')
        self.btnClear = wx.Button(self,-1,'Delete')
        self.btnOksession =wx.Button(self,-1,'OK')

        sb1 = wx.StaticBox(self,-1,'Change/View Order: ',size=(700,100))
        boxsizer = wx.StaticBoxSizer(sb1, wx.HORIZONTAL)


        self.sessionNo = wx.StaticText(self,-1,'Order No: 1')
        sizer4.Add(self.sessionNo,pos=(0,0),flag=wx.EXPAND | wx.ALL, border=5)
        sb2 = wx.StaticBox(self,-1,size=(500,500))
        boxsizer2 = wx.StaticBoxSizer(sb2, wx.VERTICAL)

        text2 = wx.StaticText(self,-1,'Order No: ')
        self.sessionText = wx.TextCtrl(self)
        self.btnSession = wx.Button(self,-1,'OK')
        boxsizer.Add(text2,flag= wx.EXPAND | wx.ALL, border=5)
        boxsizer.Add(self.sessionText,flag=wx.EXPAND | wx.ALL,border=5)
        boxsizer.Add(self.btnSession, flag=wx.EXPAND | wx.ALL,border=5)

        sizer1.Add(txt1, pos=(0,0), flag=wx.TOP | wx.LEFT | wx.RIGHT, border=5)
        sizer1.Add(self.textQuantity,pos=(0,1),flag = wx.TOP | wx.RIGHT,border=5)
        sizer1.Add(self.qInx,pos=(0,2),flag = wx.TOP | wx.RIGHT,border=5)
        sizer1.Add(self.qDx,pos=(0,3),flag = wx.TOP | wx.RIGHT,border=5)
        sizer1.Add(self.btnOksession,pos=(0,4),flag = wx.TOP | wx.RIGHT,border=5)
        sizer2.Add(self.quantityStatus, pos=(0,5), flag=wx.TOP | wx.LEFT | wx.RIGHT, border=5)
        sizer3.Add(self.okButton, pos=(0,6), flag=wx.TOP | wx.LEFT | wx.RIGHT, border=5)
        sizer3.Add(self.btnClear, pos=(0,7), flag=wx.TOP | wx.LEFT | wx.RIGHT, border=5)

        boxsizer2.Add(sizer1,flag= wx.EXPAND | wx.ALL, border=5)
        boxsizer2.Add(sizer4,flag=wx.EXPAND | wx.ALL, border = 5)
        boxsizer2.Add(sizer2,flag=wx.EXPAND | wx.ALL,border=5)
        boxsizer2.Add(sizer3, flag=wx.EXPAND | wx.ALL,border=5)

        self.sizer.Add(boxsizer2,pos=(0,0),flag= wx.TOP | wx.RIGHT, border=5)
        self.sizer.Add(boxsizer,pos=(1,0),flag= wx.TOP | wx.RIGHT, border=5)

        self.SetSizer(self.sizer)
        self.Fit()

    def setZero(self):
        self.textQuantity.SetValue('1')


class leftContent(wx.Panel):
    def __init__(self,parent,id):
        wx.Panel.__init__(self,parent,id)
        self.container = wx.BoxSizer(wx.VERTICAL)
        sb = wx.StaticBox(self,-1,size=(300,200))
        boxsizer = wx.StaticBoxSizer(sb, wx.VERTICAL)
        self.textSearch = wx.TextCtrl(self,size=(250,20))
        self.textSearch.Bind(wx.EVT_KEY_UP, self.searchFilter)
        btnSearch = wx.Button(self,-1,'Search')
        sc = wx.GridBagSizer(1,1)

        self.list = CheckListCtrl(self)
        self.list.SetSize((100,200))
        self.list.InsertColumn(0, '', width=140)

        for i in mylist:
            self.list.InsertStringItem(sys.maxint, i)

        sc.Add(self.textSearch,pos=(0,0),flag=wx.EXPAND | wx.ALL,border=5)
        sc.Add(btnSearch,pos=(0,1),flag=wx.EXPAND | wx.ALL, border=5)
        boxsizer.Add(sc, flag=wx.EXPAND | wx.ALL)
        boxsizer.Add(self.list, flag=wx.EXPAND | wx.ALL,border=10)
        self.container.Add(boxsizer, wx.EXPAND | wx.ALL,border=10)

        self.SetSizer(self.container)

    def searchFilter(self,event):
        word = self.textSearch.GetValue()
        i = 0
        newList = []
        for row in sale.lists():
            if word in row[i]:
                newList.append(row[i])
        self.list.DeleteAllItems()

        for item in newList:
            self.list.InsertStringItem(self.list.GetItemCount(), item)