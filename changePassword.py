#!/user/bin/python

import wx
from security import AccountManager


class ChangePassword(wx.Frame):

    def __init__(self,parent,id,title):
        super(ChangePassword, self).__init__(parent, title=title,style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER)
        self.manager = AccountManager()
        self.choices = self.populateNames()
        panel = wx.Panel(self,-1)
        hb1 = wx.BoxSizer(wx.VERTICAL)
        fgs = wx.FlexGridSizer(5, 2, 20, 0)
        username = wx.StaticText(panel, 1, 'UserName: ')
        self.nameText = wx.Choice(panel,1,choices=self.choices,style = wx.CB_READONLY,size = (5,30))
        self.oldPassword = wx.StaticText(panel, 1, 'Old Password: ')
        self.oldPasswordText = wx.TextCtrl(panel, size=(180, 30),style=wx.TE_PASSWORD)
        self.newPassword = wx.StaticText(panel, 1, 'New Password: ')
        self.newPasswordText = wx.TextCtrl(panel, size=(180, 30),style=wx.TE_PASSWORD)
        self.status = wx.StaticText(panel, 1, '')
        self.Save = wx.Button(panel, 1, 'SAVE CHANGES')
        self.Save.SetBackgroundColour('green')
        self.Save.Bind(wx.EVT_BUTTON,self.saveButtonHandeler)

        fgs.AddMany([(username), (self.nameText, 1, wx.EXPAND), (self.oldPassword), (self.oldPasswordText, 1, wx.EXPAND), (self.newPassword), (self.newPasswordText, 1, wx.EXPAND), (self.status),(self.Save)])
        hb1.Add(fgs, 0, wx.SHAPED | wx.TOP, 40)
        panel.SetSizer(hb1)
        panel.SetSize((850,400))
        self.Centre()
        self.SetSize((400,450))
        self.Show(True)

    def populateNames(self):
        choices = []
        for row in self.manager.getUserNames():
            choices.append(row[0])
        return choices

    def saveButtonHandeler(self,event):
        name = self.nameText.GetString( self.nameText.GetSelection())
        password = self.newPasswordText.GetValue()
        if self.manager.getOldPassword(name)[0][0] == self.oldPasswordText.GetValue() :
            self.manager.setName(name)
            self.manager.setPassword(password)
            self.manager.changePassword()
            self.status.SetLabel('0K')
            self.nameText.SetValue('')
            self.status.SetLabel('Password changed added successfully')
            self.oldPasswordText.SetValue('')
            self.newPasswordText.SetValue('')
        else:
            self.status.SetLabel('WRONG OLD PASSWORD PLEASE ENTER AGAIN')
            print 'NOT OK'
if __name__ == '__main__':
    app = wx.App()
    change = ChangePassword(None,1,'CHANGE PASSWORD')
    app.MainLoop()

