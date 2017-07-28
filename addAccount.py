#!/user/bin/python
import wx
from security import AccountManager


class AddAccount(wx.Panel):

    def __init__(self,parent,id):
        super(AddAccount, self).__init__(parent,id)
        box = wx.GridBagSizer(1,1)

        hb1 = wx.StaticBox(self,-1,'Add New Acount')
        boxsizer= wx.StaticBoxSizer(hb1,wx.VERTICAL)
        fgs = wx.FlexGridSizer(6, 2, 5, 2)
        username = wx.StaticText(self, 1, 'UserName:')
        self.nameText = wx.TextCtrl(self, size=(100, 30))
        self.newPasswordsTextCtrl()
        self.space = wx.StaticText(self, 1, '')
        self.list =['Administrator','Sales']
        self.sta = wx.RadioBox(self, label='Status', size=(200, 50), choices=self.list,
                               majorDimension=1, style=wx.RA_SPECIFY_ROWS)
        self.status = wx.StaticText(self, 1, '')
        self.status1 = wx.StaticText(self, 1, '')
        self.status2 = wx.StaticText(self, 1, '')
        self.Save = wx.Button(self, 1, 'SAVE CHANGES')
        self.Save.Bind(wx.EVT_BUTTON,self.saveButtonHandeler)
        self.text_password1.Bind(wx.EVT_KEY_UP, self.keyReleased3)
        self.text_no_password1.Bind(wx.EVT_KEY_UP, self.keyReleased1)

        fgs.AddMany([(username),(self.nameText,1,wx.EXPAND),(self.newPassword),(self.sizer1)
                     ,(self.status1),(self.sta),(self.check),(self.status2),(self.Save),self.status])
        boxsizer.Add(fgs, 1, flag=wx.EXPAND | wx.ALL, border=5)
        box.Add(boxsizer,pos=(0,2),flag=wx.EXPAND | wx.ALL,border=5)
        self.SetSizer(box)

    def keyReleased1(self, event):
        keycode = event.GetKeyCode()
        if keycode == wx.WXK_RETURN or keycode == wx.WXK_NUMPAD_ENTER:
            self.saveButtonHandeler(event=None)
            event.EventObject.Navigate()
        else:
            self.text_password1.SetValue(self.text_no_password1.GetValue())
        event.Skip()

    def keyReleased3(self, event):
        keycode = event.GetKeyCode()
        if keycode == wx.WXK_RETURN or keycode == wx.WXK_NUMPAD_ENTER:
            self.saveButtonHandeler(event=None)
            event.EventObject.Navigate()
        else:
            self.text_no_password1.SetValue(self.text_password1.GetValue())
        event.Skip()

    def newPasswordsTextCtrl(self):
        self.password_shown1 = False
        self.sizer1 = wx.BoxSizer(wx.HORIZONTAL)
        self.newPassword = wx.StaticText(self, 1, 'Password:')
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

    def saveButtonHandeler(self,event):
        name = self.nameText.GetValue()
        password = self.text_password1.GetValue()
        if name:
            if password:
                if len(name)>=5:
                    if len(password)>=5:
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
                        self.text_password1.SetValue('')
                        self.text_no_password1.SetValue('')
                    else:
                        wx.MessageBox("Password isn't strong enough\n{chara} more character needed".format(chara=(5-len(password))))
                else:
                    wx.MessageBox("Username isn't strong enough\n{chara}  more character needed".format(chara=(5 - len(name))))
            else:
                wx.MessageBox('Enter a Password', 'INFO')
        else:
            wx.MessageBox('Enter a Username', 'INFO')
