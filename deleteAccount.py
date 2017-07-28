#!/user/bin/python

import wx
from security import AccountManager

class DeleteAccount(wx.Panel):

    def __init__(self, parent, id):
        super(DeleteAccount, self).__init__(parent,id)
        self.manager = AccountManager()
        self.choices = self.populateNames()
        hb1 = wx.GridBagSizer(1, 1)
        sb = wx.StaticBox(self,-1,'Delete Acount')
        box = wx.StaticBoxSizer(sb,wx.HORIZONTAL)

        fgs = wx.FlexGridSizer(7, 2, 5, 2)
        username = wx.StaticText(self, 1, 'Username: ')
        self.nameText = wx.Choice(self, 1, choices=self.choices, size=(5, 30))
        self.newPasswordsTextCtrl()
        self.status = wx.StaticText(self, 1, '')
        self.status1 = wx.StaticText(self, 1, '')
        self.status2 = wx.StaticText(self, 1, '')
        self.status3 = wx.StaticText(self, 1, '')
        self.status4 = wx.StaticText(self, 1, '')
        self.status5 = wx.StaticText(self, 1, '')
        self.status6 = wx.StaticText(self, 1, '')
        self.status7 = wx.StaticText(self, 1, '')
        self.Save = wx.Button(self, 1, 'DELETE')
        self.text_password1.Bind(wx.EVT_KEY_UP, self.keyReleased3)
        self.text_no_password1.Bind(wx.EVT_KEY_UP, self.keyReleased1)
        self.Save.Bind(wx.EVT_BUTTON, self.DeleteButtonHandeler)
        fgs.AddMany([(username),(self.nameText, 1, wx.EXPAND), (self.newPassword), (self.sizer1),(self.check),(self.status1),
                     (self.Save),(self.status),(self.status3),(self.status4),(self.status5),(self.status6),(self.status7)])
        box.Add(fgs,flag=wx.SHAPED | wx.TOP | wx.LEFT, border=5)
        hb1.Add(box,pos=(0,2),flag=wx.EXPAND | wx.ALL,border=5)
        self.SetSizer(hb1)

    def keyReleased1(self, event):
        keycode = event.GetKeyCode()
        if keycode == wx.WXK_RETURN or keycode == wx.WXK_NUMPAD_ENTER:
            self.DeleteButtonHandeler(event=None)
            event.EventObject.Navigate()
        else:
            self.text_password1.SetValue(self.text_no_password1.GetValue())
        event.Skip()

    def keyReleased3(self, event):
        keycode = event.GetKeyCode()
        if keycode == wx.WXK_RETURN or keycode == wx.WXK_NUMPAD_ENTER:
            self.DeleteButtonHandeler(event=None)
            event.EventObject.Navigate()
        else:
            self.text_no_password1.SetValue(self.text_password1.GetValue())
        event.Skip()

    def newPasswordsTextCtrl(self):
        self.password_shown1 = False
        self.sizer1 = wx.BoxSizer(wx.HORIZONTAL)
        self.newPassword = wx.StaticText(self, 1, 'Enter your password: ')
        self.text_password1 = wx.TextCtrl(self, style=wx.TE_PASSWORD, size=(180, 30))
        self.sizer1.Add(self.text_password1, 0, wx.ALL, 0)
        self.text_no_password1 = wx.TextCtrl(self, size=(180, 30))
        self.text_no_password1.Hide()
        self.sizer1.Add(self.text_no_password1, 0, wx.ALL, 0)
        self.check = wx.CheckBox(self, -1, 'SHOW PASSWORD')
        self.check.Bind(wx.EVT_CHECKBOX, self.onCheck)


    def onCheck(self, event):
        self.text_password1.Show(self.password_shown1)
        self.text_no_password1.Show(not self.password_shown1)
        if not self.password_shown1:
            self.text_no_password1.SetValue(self.text_password1.GetValue())
            self.text_no_password1.SetFocus()
        else:
            self.text_password1.SetValue(self.text_no_password1.GetValue())
            self.text_password1.SetFocus()
        self.text_password1.GetParent().Layout()
        self.password_shown1 = not self.password_shown1

    def populateNames(self):
        choices = []
        for row in self.manager.getUserNames():
            choices.append(row[0])
        return choices

    def DeleteButtonHandeler(self, event):
        index = self.nameText.GetSelection()
        if index != -1:
            if self.text_no_password1.GetValue():
                name = self.nameText.GetString(index)
                self.manager.setName(name)
                if self.manager.getLoginAcc()[0] == self.text_no_password1.GetValue():
                    self.manager.deleteAccount()
                    self.status.SetLabel('Account deleted successfully')
                    self.nameText.Clear()
                    myList = self.populateNames()
                    for item in myList:
                        self.nameText.Append(item)
                else:
                    self.status.SetLabel('Wrong password!')
            else:
                wx.MessageBox('Enter your login password', 'INFO')
        else:
            wx.MessageBox('Select an Account', 'INFO')

