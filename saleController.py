#!/user/bin/python
import wx
import sys
from wx.lib.mixins.listctrl import CheckListCtrlMixin, ListCtrlAutoWidthMixin
from salesHandler import SalesHandler
from salesHandler import Sales


sale = SalesHandler()
mylist = []
for row in sale.lists():
    mylist.append(row[0])

class CheckListCtrl(wx.ListCtrl, CheckListCtrlMixin, ListCtrlAutoWidthMixin):
    def __init__(self, parent):
        wx.ListCtrl.__init__(self, parent, -1, style=wx.LC_REPORT | wx.SUNKEN_BORDER,size=(200,700))
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
        self.quantityStatus = wx.TextCtrl(self,size=(600,400),style=wx.TE_MULTILINE | wx.TE_READONLY)
        self.okButton = wx.Button(self,-1,'OK')
        self.btnClear = wx.Button(self,-1,'Clear')
        self.btnOksession =wx.Button(self,-1,'OK')

        sb1 = wx.StaticBox(self,-1,'Change Session',size=(700,100))
        boxsizer = wx.StaticBoxSizer(sb1, wx.HORIZONTAL)

        self.session = 0
        sessionNo = wx.StaticText(self,-1,'Session No: '+str(self.session))
        sizer4.Add(sessionNo,pos=(0,0),flag=wx.EXPAND | wx.ALL, border=5)
        sb2 = wx.StaticBox(self,-1,size=(500,500))
        boxsizer2 = wx.StaticBoxSizer(sb2, wx.VERTICAL)

        text2 = wx.StaticText(self,-1,'Session No: ')
        sessionText = wx.TextCtrl(self)
        btnSession = wx.Button(self,-1,'OK')
        boxsizer.Add(text2,flag= wx.EXPAND | wx.ALL, border=5)
        boxsizer.Add(sessionText,flag=wx.EXPAND | wx.ALL,border=5)
        boxsizer.Add(btnSession, flag=wx.EXPAND | wx.ALL,border=5)

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

    def setZero(self):
        self.textQuantity.SetValue('0')


class leftContent(wx.Panel):
    def __init__(self,parent,id):
        wx.Panel.__init__(self,parent,id)
        self.container = wx.BoxSizer(wx.VERTICAL)
        sb = wx.StaticBox(self,-1,size=(300,700))
        boxsizer = wx.StaticBoxSizer(sb, wx.VERTICAL)
        self.textSearch = wx.TextCtrl(self,size=(250,20))
        self.textSearch.Bind(wx.EVT_KEY_UP, self.searchFilter)
        btnSearch = wx.Button(self,-1,'Search')
        sc = wx.GridBagSizer(1,1)

        self.list = CheckListCtrl(self)
        self.list.SetSize((500,200))
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


class Content(wx.Panel):
    def __init__(self, parent, id):
        wx.Panel.__init__(self, parent, id, size=(1500, 1000))
        self.box = wx.GridBagSizer(3,1)
        txt = wx.StaticText(self, -1, 'Drinks Management System')

        stline = wx.StaticLine(self)
        self.box.Add(txt, pos=(0,1), flag=wx.EXPAND | wx.TOP, border=3)
        self.box.Add(stline, pos=(1,0),span=(1,5),flag=wx.EXPAND | wx.BOTTOM, border=0)

        self.leftContent = leftContent(self,-1)
        self.rightContent = rightContent(self,-1)
        self.leftContent.list.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnSelectItem)
        self.rightContent.qInx.Bind(wx.EVT_BUTTON, self.AddButton)
        self.rightContent.qDx.Bind(wx.EVT_BUTTON, self.SubButton)
        self.rightContent.btnClear.Bind(wx.EVT_BUTTON, self.OnSeleClear)
        self.rightContent.btnOksession.Bind(wx.EVT_BUTTON, self.OnSeleOkButton)
        self.box.Add(self.leftContent,pos=(2,0),flag= wx.EXPAND | wx.ALL, border=10)
        self.box.Add(self.rightContent,pos=(2,1),flag= wx.EXPAND | wx.ALL, border=10)
        self.SetSizer(self.box, wx.EXPAND | wx.ALL, )

    def OnSelectItem(self, event):
        self.rightContent.setZero()

    def AddButton(self,event):
        value = self.rightContent.textQuantity.GetValue()
        if value:
            newValue = int(value)
            if newValue >= 0:
                newValue += 1
                self.rightContent.textQuantity.SetValue(str(newValue))
            else:
                self.rightContent.textQuantity.SetValue('0')
        else:
            self.rightContent.textQuantity.SetValue('1')

    def SubButton(self,event):
        value = self.rightContent.textQuantity.GetValue()
        if value:
            newValue = int(value)
            if newValue > 0:
                newValue -= 1
                self.rightContent.textQuantity.SetValue(str(newValue))
            else:
                self.rightContent.textQuantity.SetValue('0')
        else:
            self.rightContent.textQuantity.SetValue('1')

    def OnSeleOkButton(self, event):
        index = self.leftContent.list.GetFirstSelected()
        try:
            float(self.rightContent.textQuantity.GetValue())
            if index != -1:
                self.sale = Sales(self.leftContent.list.GetItemText(index), self.rightContent.textQuantity.GetValue())
                self.rightContent.quantityStatus.AppendText('{name}\t{Quantity}\t{total}\n'.format(
                    name=self.sale.getName() ,Quantity=self.sale.getAmount(),total=self.sale.getTotalCost()))
            else:
                wx.MessageBox('Please select a drink', 'Error')
        except ValueError:
            wx.MessageBox('Wrong Amount')

    def OnSeleClear(self,event):
        self.rightContent.quantityStatus.SetValue('')


