#!/user/bin/python
# treectrlwithsplitter.py

import wx
from leftContent import leftContent
from rightContent import rightContent




class classMain(wx.Frame):

	def __init__(self, parent, id, title):
		wx.Frame.__init__(self, parent, id, title, size=(800,600))
		self.createMenu()
		panel = wx.Panel(self, -1)
		sizer = wx.BoxSizer(wx.HORIZONTAL)
		self.SetSizer(sizer)
		sizer.SetOrientation(wx.HORIZONTAL)
		self.rightContent = rightContent(panel, -1)
		self.leftContent = leftContent(panel, -1)
		sizer.Add(self.leftContent,-1, wx.EXPAND | wx.ALL)
		sizer.Add(self.rightContent,-1, wx.EXPAND | wx.ALL)
		self.SetSize((800, 600))
		self.Centre()
		self.Show(True)

	def createMenu(self):
		menuBar = wx.MenuBar()
		fileMenu = wx.Menu()
		fitem = fileMenu.Append(wx.ID_EXIT, 'Quit', 'Quit application')
		menuBar.Append(fileMenu, '&File')
		editMenu = wx.Menu()
		edit = editMenu.Append(wx.ID_EXIT, 'Edit', 'Quit application')
		menuBar.Append(editMenu, '&Edit')
		self.SetMenuBar(menuBar)


if __name__ == "__main__":
	app = wx.App()
	classMain(None, -1, 'Drinks Management System')
	app.MainLoop()