#!/user/bin/python
import wx

class mainControll(wx.Frame):
	"""docstring for mainControll"""
	def __init__(self, parent,id,title):
		super(mainControll, self).__init__(parent,title= title,size=(800,700))
		self.panel = wx.Panel(self)

		self.menuBar()
		self.Centre()
		self.Show()

	def menuBar(self):
		menubar = wx.MenuBar()
		file = wx.Menu()
		filehelp = wx.Menu()
		fileabout = wx.Menu()

		new = file.Append(wx.ID_NEW, 'New','New Session')
		exit = file.Append(wx.ID_EXIT,'Quit','Quit Application')

		about = fileabout.Append(wx.ID_ABOUT, 'About','About Application')
		fhelp = filehelp.Append(wx.ID_HELP,'Help','Help')
		menubar.Append(file,'&File')
		menubar.Append(fileabout,'&About')
		menubar.Append(filehelp,'&Help')
		self.SetMenuBar(menubar)
		

def main():
	app = wx.App()
	mainControll(None, 1,'Drinks Management System')
	app.MainLoop()

if __name__ == '__main__':
		main()	
		