#!/user/bin/python
import wx
from  rightContent import Content1
from changePassword import ChangePassword
from reportView import report
from side2 import salew

class windowAdmin(wx.Frame):
    def __init__(self, parent):
        super(windowAdmin, self).__init__(parent, title='GMS - "Huduma Chap Chap"',size=(250, 150))

        self.menuBar()
        self.InitUI()

    def InitUI(self):
        nb = wx.Notebook(self, style=wx.NB_TOP)
        self.content = salew(nb,-1)
        self.content1 = Content1(nb,-1)
        self.pswChange = ChangePassword(nb,-1)
        self.report = report(nb,-1)

        nb.AddPage(self.content1, "Stock Update")
        nb.AddPage(self.content, "Sales Management")
        nb.AddPage(self.pswChange, "Settings")
        nb.AddPage(self.report, " View Reports")

        self.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED,self.onTabchange)
        self.Maximize(True)
        self.Centre()
        self.Hide()

    def menuBar(self):
        menubar = wx.MenuBar()
        file = wx.Menu()
        filehelp = wx.Menu()
        fileabout = wx.Menu()

        file.AppendSeparator()
        self.logout = file.Append(wx.ID_ABORT, 'Log out', 'Log out')
        self.exit = file.Append(wx.ID_EXIT, 'Close', 'Quit Application')

        about = fileabout.Append(wx.ID_ABOUT, 'About', 'About Application')
        fhelp = filehelp.Append(wx.ID_HELP, 'Help', 'Help')
        menubar.Append(file, '&File')
        menubar.Append(fileabout, '&About')
        menubar.Append(filehelp, '&Help')
        self.SetMenuBar(menubar)

    def onTabchange(self,e):
        self.report.refresh()