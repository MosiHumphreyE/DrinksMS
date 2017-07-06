#!/user/bin/python
import wx
from saleController import Content
from  rightContent import Content1
from changePassword import ChangePassword
from addAccount import AddAccount
from deleteAccount import DeleteAccount

class windowAdmin(wx.Frame):
    def __init__(self, parent):
        super(windowAdmin, self).__init__(parent, title='Drinks Management System',size=(250, 150))

        self.menuBar()
        self.InitUI()

    def InitUI(self):
        nb = wx.Notebook(self, style=wx.NB_LEFT)
        self.content = Content(nb,-1)
        self.content1 = Content1(nb,-1)
        self.pswChange = ChangePassword(nb,-1)

        nb.AddPage(self.content1, "Stock Update")
        nb.AddPage(self.content, "Sales Management")
        nb.AddPage(self.pswChange, "Account management")



        self.Maximize(True)
        self.Centre()
        self.Hide()

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
