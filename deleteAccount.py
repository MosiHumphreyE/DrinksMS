#!/user/bin/python

import wx
from security import AccountManager

class DeleteAccount(wx.Frame):

    def __init__(self,parent,id,title):
        super(DeleteAccount, self).__init__(parent, title=title, style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER)
        self.manager = AccountManager()
        self.choices = self.populateNames()
        panel = wx.Panel(self, -1)
        hb1 = wx.BoxSizer(wx.VERTICAL)
        fgs = wx.FlexGridSizer(5, 2, 20, 0)
        username = wx.StaticText(panel, 1, 'Username: ')
        self.nameText = wx.Choice(panel, 1, choices=self.choices, style=wx.CB_READONLY, size=(5, 30))
        self.status = wx.StaticText(panel, 1, '')
        self.status1 = wx.StaticText(panel, 1, '')
        self.status2 = wx.StaticText(panel, 1, '')
        self.Save = wx.Button(panel, 1, 'DELETE')
        self.Save.SetBackgroundColour('green')
        self.Save.Bind(wx.EVT_BUTTON, self.DeleteButtonHandeler)

        fgs.AddMany([username, (self.nameText, 1, wx.EXPAND), self.status, self.Save])
        hb1.Add(fgs, 0, wx.SHAPED | wx.TOP, 40)
        panel.SetSizer(hb1)
        panel.SetSize((850, 400))
        self.Centre()
        self.SetSize((400, 450))
        self.Show(True)

    def populateNames(self):
        choices = []
        for row in self.manager.getUserNames():
            choices.append(row[0])
        return choices

    def DeleteButtonHandeler(self, event):
        name = self.nameText.GetString(self.nameText.GetSelection())
        self.manager.setName(name)
        self.manager.deleteAccount()
        self.status.SetLabel('Account deleted successfully')

if __name__ == '__main__':
    app = wx.App()
    delete = DeleteAccount(None, 1, 'DELETE ACCOUNT')
    app.MainLoop()

