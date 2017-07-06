#!/user/bin/python

import wx
from security import AccountManager
from addAccount import AddAccount
from deleteAccount import DeleteAccount

class ChangePassword(wx.Panel):

    def __init__(self,parent,id):
        super(ChangePassword, self).__init__(parent,id,style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER)
        self.manager = AccountManager()
        self.choices = self.populateNames()
        sb = wx.StaticBox(self,-1,'Change Password')
        sbox = wx.StaticBoxSizer(sb,wx.VERTICAL)
        self.addAcc = AddAccount(self, -1)
        self.deleAcc = DeleteAccount(self, -1)
        hb1 = wx.GridBagSizer(2,2)
        hb1.Add(self.addAcc, pos=(0, 2), flag=wx.EXPAND | wx.ALL, border=20)
        hb1.Add(self.deleAcc, pos=(0, 4), flag=wx.EXPAND | wx.ALL, border=20)
        fgs = wx.FlexGridSizer(6, 2, 10, 10)
        username = wx.StaticText(self, 1, 'UserName: ')
        self.nameText = wx.Choice(self,1,choices=self.choices,style = wx.CB_READONLY,size = (5,30))
        self.passwordsTextCtrl()
        self.newPasswordsTextCtrl()
        self.status = wx.StaticText(self, 1, '')
        self.sta1 = wx.StaticText(self, 1, '')
        self.sta2 = wx.StaticText(self, 1, '')
        self.Save = wx.Button(self, 1, 'SAVE CHANGES')
        self.Save.SetBackgroundColour('green')
        self.Save.Bind(wx.EVT_BUTTON, self.saveButtonHandeler)
        self.text_no_password.Bind(wx.EVT_KEY_UP, self.keyReleased)
        self.text_password.Bind(wx.EVT_KEY_UP, self.keyReleased2)
        self.text_password1.Bind(wx.EVT_KEY_UP, self.keyReleased3)
        self.text_no_password1.Bind(wx.EVT_KEY_UP, self.keyReleased1)

        fgs.AddMany([(username), (self.nameText, 1, wx.EXPAND), (self.oldPassword, 1, wx.EXPAND), (self.sizer), (self.newPassword, 1, wx.EXPAND), (self.sizer1),
                     (self.check), (self.sta1) ,(self.status),(self.sta2),(self.Save)])
        sbox.Add(fgs,flag= wx.SHAPED | wx.TOP | wx.LEFT | wx.BOTTOM, border=40)
        hb1.Add(sbox,pos=(1,2),flag=wx.EXPAND | wx.ALL, border=5)
        self.SetSizer(hb1)

    def keyReleased(self,event):
        self.text_password.SetValue(self.text_no_password.GetValue())

    def keyReleased2(self,event):
        self.text_no_password.SetValue(self.text_password.GetValue())

    def keyReleased1(self,event):
        self.text_password1.SetValue(self.text_no_password1.GetValue())

    def keyReleased3(self,event):
        self.text_no_password1.SetValue(self.text_password1.GetValue())



    def populateNames(self):
        choices = []
        for row in self.manager.getUserNames():
            choices.append(row[0])
        return choices

    def passwordsTextCtrl(self):
        self.password_shown = False
        self.sizer= wx.BoxSizer(wx.HORIZONTAL)
        self.oldPassword = wx.StaticText(self, 1, 'Old Password: ')
        self.text_password = wx.TextCtrl(self, style=wx.TE_PASSWORD, size = (180,30))
        self.sizer.Add(self.text_password,0,wx.ALL,0)
        self.text_no_password = wx.TextCtrl(self, size = (180,30))
        self.text_no_password.Hide()
        self.sizer.Add(self.text_no_password,0,wx.ALL,0)
        self.check = wx.CheckBox(self, -1, 'SHOW PASSWORD')
        self.check.Bind(wx.EVT_CHECKBOX, self.onCheck)

    def newPasswordsTextCtrl(self):
        self.password_shown1 = False
        self.sizer1= wx.BoxSizer(wx.HORIZONTAL)
        self.newPassword = wx.StaticText(self, 1, 'New Password: ')
        self.text_password1 = wx.TextCtrl(self, style=wx.TE_PASSWORD, size = (180,30))
        self.sizer1.Add(self.text_password1,0,wx.ALL,0)
        self.text_no_password1 = wx.TextCtrl(self, size = (180,30))
        self.text_no_password1.Hide()
        self.sizer1.Add(self.text_no_password1,0,wx.ALL,0)


    def saveButtonHandeler(self,event):
        name = self.nameText.GetString( self.nameText.GetSelection())
        password = self.text_password1.GetValue()
        if self.manager.getOldPassword(name)[0][0] == self.text_password.GetValue():
            self.manager.setName(name)
            self.manager.setPassword(password)
            self.manager.changePassword()
            self.status.SetLabel('0K')
            self.status.SetLabel('Password changed added successfully')
            self.text_password1.SetValue('')
            self.text_no_password1.SetValue('')
            self.text_password.SetValue('')
            self.text_no_password.SetValue('')
        else:
            self.status.SetLabel('WRONG OLD PASSWORD PLEASE ENTER AGAIN')



    def onCheck(self,event):
        self.text_password.Show(self.password_shown)
        self.text_no_password.Show(not self.password_shown)
        if not self.password_shown:
            self.text_no_password.SetValue(self.text_password.GetValue())
            self.text_no_password.SetFocus()
        else:
            self.text_password.SetValue(self.text_no_password.GetValue())
            self.text_password.SetFocus()
        self.text_password.GetParent().Layout()
        self.password_shown = not self.password_shown
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

