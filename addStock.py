#!/user/bin/python

import wx


class AddStock(wx.Panel):
    def __init__(self,parent,id):
        wx.Panel.__init__(self, parent, id, style=wx.BORDER_THEME)
        panelSizer = wx.BoxSizer(wx.VERTICAL)
        nameTextField = wx.TextCtrl(self,-1,'')
        nameLabel = wx.StaticText(self,label = "Name")
        quantityTextField = wx.TextCtrl(self, -1, );
        quantityLabel = wx.StaticText(self, label="Quantity")
        dateTextField = wx.TextCtrl(self, -1, );
        dateLabel = wx.StaticText(self, label="Date")
        saveButton = wx.Button(self, label = "Save")
        wSizer = wx.BoxSizer(wx.HORIZONTAL)
        wSizer1 = wx.BoxSizer(wx.HORIZONTAL)
        wSizer2 = wx.BoxSizer(wx.HORIZONTAL)
        wSizer3 = wx.BoxSizer(wx.HORIZONTAL)
        wSizer.Add(nameLabel)
        wSizer.Add(nameTextField)
        wSizer1.Add(quantityLabel)
        wSizer1.Add(quantityTextField)
        wSizer2.Add(dateLabel)
        wSizer2.Add(dateTextField)
        wSizer3.Add(saveButton)
        panelSizer.Add(wSizer)
        panelSizer.Add(wSizer1)
        panelSizer.Add(wSizer2)
        panelSizer.Add(wSizer3)
        self.SetSizer( panelSizer)
        self.SetBackgroundColour(wx.RED)
        #self.SetSize((220, 900))


