#!/user/bin/python

import wx
from addStock import AddStock

class rightContent(wx.Panel):
	"""docstring for rightContent"""

	def __init__(self, parent, id):
		
		wx.Panel.__init__(self, parent, id, style=wx.BORDER_SUNKEN)
		sizer = wx.BoxSizer(wx.HORIZONTAL)
		addpanel = AddStock(self,-1)
		sizer.Add(addpanel, -1, wx.EXPAND | wx.ALL)
		self.SetSizer(sizer)
		#self.SetSize((220, 900))

		