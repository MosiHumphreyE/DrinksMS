#!/user/bin/python
import wx
from security import AccountManager


class AddAccount(wx.Frame):

    def __init__(self,parent,id,title):
        super(AddAccount, self).__init__(parent, title=title, style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER)
        panel = wx.Panel(self,-1)
        hb1 = wx.BoxSizer(wx.VERTICAL)
        fgs = wx.FlexGridSizer(4, 2, 20, 0)
        username = wx.StaticText(panel, 1, 'UserName: ')
        self.nameText = wx.TextCtrl(panel, size=(100, 30))
        self.Password = wx.StaticText(panel, 1, 'Password: ')
        self.PasswordText = wx.TextCtrl(panel, size=(100, 30), style=wx.TE_PASSWORD)
        self.space = wx.StaticText(panel, 1, '')
        self.list =['Administrator','Sales']
        self.sta = wx.RadioBox(panel, label='STATUS', size=(200, 50), choices=self.list, majorDimension=1, style=wx.RA_SPECIFY_ROWS)
        self.status = wx.StaticText(panel, 1, '')
        self.Save = wx.Button(panel, 1, 'SAVE CHANGES')
        self.Save.SetBackgroundColour('green')
        self.Save.Bind(wx.EVT_BUTTON,self.saveButtonHandeler)

        fgs.AddMany([username, (self.nameText, 1, wx.EXPAND), self.Password, (self.PasswordText, 1, wx.EXPAND), self.space, self.sta, self.status, self.Save])
        hb1.Add(fgs, 0, wx.SHAPED | wx.TOP, 40)
        panel.SetSizer(hb1)
        panel.SetSize((400,400))
        self.Centre()
        self.SetSize((400,450))
        self.Show(True)

    def saveButtonHandeler(self,event):
        name = self.nameText.GetValue()
        password = self.PasswordText.GetValue()
        manager = AccountManager()
        manager.setName(name)
        manager.setPassword(password)
        self.status1 = None
        if self.sta.GetStringSelection() == 'Administrator':
            self.status1 = 'admin'
        else:
            self.status1 = 'sales'
        manager.addAccount(self.status1)
        self.status.SetLabel('Account added successfully')
        self.nameText.SetValue('')
        self.PasswordText.SetValue('')

if __name__ == '__main__':
    app = wx.App()
    add = AddAccount(None, 1, 'ADD ACCOUNT')
    app.MainLoop()