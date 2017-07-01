#!/user/bin/python
import wx
import sys
from wx.lib.mixins.listctrl import CheckListCtrlMixin, ListCtrlAutoWidthMixin

mylist = ['list1','list2','list3','list4','list5','list6','list7','list8','list9','list10']

class CheckListCtrl(wx.ListCtrl, CheckListCtrlMixin, ListCtrlAutoWidthMixin):
    def __init__(self, parent):
        wx.ListCtrl.__init__(self, parent, -1, style=wx.LC_REPORT | wx.SUNKEN_BORDER,size=(200,700))
        CheckListCtrlMixin.__init__(self)
        ListCtrlAutoWidthMixin.__init__(self)

class Content(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,size=(800,700))
        self.panel = wx.Panel(self)
        self.box = wx.GridBagSizer(10,10)
        self.menuBar()
        txt = wx.StaticText(self.panel,-1,'Drinks Management System')

        stline= wx.StaticLine(self.panel)
        self.box.Add(txt,pos=(0,1), flag=wx.EXPAND | wx.TOP, border=3)
        self.box.Add(stline,pos=(1,0),span=(1,5),flag=wx.EXPAND | wx.BOTTOM, border=0)

        self.box.Add(self.leftContent(),pos=(2,0),flag=wx.EXPAND | wx.ALL,border=5)
        self.box.Add(self.rightContent(),pos=(2,1),flag=wx.EXPAND | wx.ALL,border=5)
        self.panel.SetSizer(self.box,wx.EXPAND | wx.ALL)
        self.Centre()
        self.Show()

    def rightContent(self):
        self.sizer = wx.GridBagSizer(5,5)
        sizer1 = wx.GridBagSizer(5,5)
        sizer2 = wx.GridBagSizer(5,5)
        sizer3 = wx.GridBagSizer(7,7)
        txt1 = wx.StaticText(self.panel,-1,'Quantity')
        textQuantity = wx.TextCtrl(self.panel)
        qInx = wx.Button(self.panel,-1,'+')
        qDx = wx.Button(self.panel,-1,'-')
        quantityStatus = wx.TextCtrl(self.panel,size=(600,500),style=wx.TE_MULTILINE)
        okButton = wx.Button(self.panel,-1,'OK')
        btnClear = wx.Button(self.panel,-1,'Clear')

        sb1 = wx.StaticBox(self.panel,-1,'Chage Session',size=(700,100))
        boxsizer = wx.StaticBoxSizer(sb1, wx.HORIZONTAL)

        sb2 = wx.StaticBox(self.panel,-1,size=(500,500))
        boxsizer2 = wx.StaticBoxSizer(sb2, wx.VERTICAL)

        text2 = wx.StaticText(self.panel,-1,'Session No: ')
        sessionText = wx.TextCtrl(self.panel)
        btnSession = wx.Button(self.panel,-1,'OK')
        boxsizer.Add(text2,flag= wx.EXPAND | wx.ALL, border=5)
        boxsizer.Add(sessionText,flag=wx.EXPAND | wx.ALL,border=5)
        boxsizer.Add(btnSession, flag=wx.EXPAND | wx.ALL,border=5)

        sizer1.Add(txt1, pos=(0,0), flag=wx.TOP | wx.LEFT | wx.RIGHT, border=5)
        sizer1.Add(textQuantity,pos=(0,1),flag = wx.TOP | wx.RIGHT,border=5)
        sizer1.Add(qInx,pos=(0,2),flag = wx.TOP | wx.RIGHT,border=5)
        sizer1.Add(qDx,pos=(0,3),flag = wx.TOP | wx.RIGHT,border=5)
        sizer2.Add(quantityStatus, pos=(0,5), flag=wx.TOP | wx.LEFT | wx.RIGHT, border=5)
        sizer3.Add(okButton, pos=(0,6), flag=wx.TOP | wx.LEFT | wx.RIGHT, border=5)
        sizer3.Add(btnClear, pos=(0,7), flag=wx.TOP | wx.LEFT | wx.RIGHT, border=5)

        boxsizer2.Add(sizer1,flag= wx.EXPAND | wx.ALL, border=5)
        boxsizer2.Add(sizer2,flag=wx.EXPAND | wx.ALL,border=5)
        boxsizer2.Add(sizer3, flag=wx.EXPAND | wx.ALL,border=5)

        self.sizer.Add(boxsizer2,pos=(0,0),flag= wx.TOP | wx.RIGHT, border=5)
        self.sizer.Add(boxsizer,pos=(1,0),flag= wx.TOP | wx.RIGHT, border=5)

        #self.panel.SetSizer(sizer)
        return self.sizer


    def leftContent(self):
        self.container = wx.BoxSizer(wx.VERTICAL)
        sb = wx.StaticBox(self.panel,-1,size=(550,700))
        boxsizer = wx.StaticBoxSizer(sb, wx.VERTICAL)
        textSearch = wx.TextCtrl(self.panel,size=(250,20))
        btnSearch = wx.Button(self.panel,-1,'Search')
        sc = wx.GridBagSizer(1,1)

        self.list = CheckListCtrl(self.panel)
        self.list.SetSize((500,200))
        self.list.InsertColumn(0, '', width=140)

        for i in mylist:
            self.list.InsertStringItem(sys.maxint, i)

        sc.Add(textSearch,pos=(0,0),flag=wx.EXPAND | wx.ALL,border=5)
        sc.Add(btnSearch,pos=(0,1),flag=wx.EXPAND | wx.ALL, border=5)
        boxsizer.Add(sc, flag=wx.EXPAND | wx.ALL)
        boxsizer.Add(self.list, flag=wx.EXPAND | wx.ALL,border=10)
        self.container.Add(boxsizer, wx.EXPAND | wx.ALL,border=10)

        return self.container

    def menuBar(self):
        menubar = wx.MenuBar()
        file = wx.Menu()
        filehelp = wx.Menu()
        fileabout = wx.Menu()

        new = file.Append(wx.ID_NEW, 'New', 'New Session')
        file.AppendSeparator()
        exit = file.Append(wx.ID_EXIT, 'Quit', 'Quit Application')

        about = fileabout.Append(wx.ID_ABOUT, 'About', 'About Application')
        fhelp = filehelp.Append(wx.ID_HELP, 'Help', 'Help')
        menubar.Append(file, '&File')
        menubar.Append(fileabout, '&About')
        menubar.Append(filehelp, '&Help')
        self.SetMenuBar(menubar)

if __name__=='__main__':
    app = wx.App()
    Content(None,-1)
    app.MainLoop()