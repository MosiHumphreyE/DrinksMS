import wx
from side2 import salew
from rightContent import updateStock
class windowSale(wx.Frame):
    def __init__(self,parent):
        super(windowSale, self).__init__(parent, title='Drinks Management System', size=(250, 150))
        self.menuBar()
        self.InitUI()

    def InitUI(self):
        self.notebook = wx.Notebook(self,style=wx.NB_TOP)
        self.stock = updateStock(self.notebook,-1)
        self.sale = salew(self.notebook,-1)

        self.notebook.AddPage(self.sale,"SALES MANAGEMENT")
        self.notebook.AddPage(self.stock,"STOCKS MANAGEMENT")
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
        self.exit = file.Append(wx.ID_EXIT, 'Quit', 'Quit Application')

        about = fileabout.Append(wx.ID_ABOUT, 'About', 'About Application')
        fhelp = filehelp.Append(wx.ID_HELP, 'Help', 'Help')
        menubar.Append(file, '&File')
        menubar.Append(fileabout, '&About')
        menubar.Append(filehelp, '&Help')
        self.SetMenuBar(menubar)
