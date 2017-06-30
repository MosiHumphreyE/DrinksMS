#!/user/bin/python

import wx
from adminTree import AdminTree


class leftContent(wx.Panel):

	def __init__(self, parent, id):
		wx.Panel.__init__(self, parent, id, style=wx.BORDER_THEME)
		tree = AdminTree(self, -1)
		sizer = wx.BoxSizer(wx.HORIZONTAL)
		sizer.Add(tree, 1, wx.EXPAND | wx.ALL)
		self.SetSizer(sizer)
		self.SetSize((220,900))

		