#!/user/bin/python
import wx

class LogIn(wx.Panel):
	"""docstring for LogIn"""
	def __init__(self, parent,id):
		super(LogIn, self).__init__(parent,id)
		self.state = False

		self.loginForm()

	def loginForm(self):
		hb1 = wx.BoxSizer(wx.VERTICAL)

		fgs = wx.FlexGridSizer(4, 2, 9, 25)
		username = wx.StaticText(self,1,'UserName')
		self.nameText = wx.TextCtrl(self,size=(180,30))
		password = wx.StaticText(self,1,'Password')
		self.passText = wx.TextCtrl(self)
		self.status = wx.StaticText(self,1,'')
		empty = wx.StaticText(self,1,'')
		logo = wx.StaticText(self,1,'Welcome Drinks Managemant Sytem')

		self.btnLogin = wx.Button(self,1,'Login')
		#self.Bind(wx.EVT_BUTTON,self.CheckPass,id=btnLogin.GetId())

		fgs.AddMany([(username),(self.nameText,1,wx.EXPAND),(password),(self.passText,1,wx.EXPAND),(empty),
			(self.btnLogin),(self.status)])
		hb1.Add(logo, 0, wx.CENTER | wx.TOP,300)
		hb1.Add(fgs,0,wx.CENTER | wx.TOP, 50)
		self.SetSizer(hb1)

		