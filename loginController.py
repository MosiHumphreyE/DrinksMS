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

		fgs = wx.FlexGridSizer(5, 2, 9, 25)
		username = wx.StaticText(self,1,'UserName')
		self.nameText = wx.TextCtrl(self,size=(180,30))
		self.password = wx.StaticText(self, 1, 'Password:')
		self.status = wx.StaticText(self,1,'')
		self.check = wx.CheckBox(self, -1, 'SHOW PASSWORD')
		self.check.Bind(wx.EVT_CHECKBOX, self.onCheck)
		empty = wx.StaticText(self,1,'')
		empty1 = wx.StaticText(self, 1, '')
		logo = wx.StaticText(self,1,'Welcome Drinks Managemant Sytem')
		self.newPasswordsTextCtrl()
		self.passText.Bind(wx.EVT_KEY_UP, self.keyReleased1)
		self.passNoText.Bind(wx.EVT_KEY_UP, self.keyReleased0)

		self.btnLogin = wx.Button(self,1,'Login')

		fgs.AddMany([(username),(self.nameText,1,wx.EXPAND),(self.password),(self.sizer,1,wx.EXPAND),(self.check),
					 (empty1), (empty),(self.btnLogin),(self.status)])
		hb1.Add(logo, 0, wx.CENTER | wx.TOP,300)
		hb1.Add(fgs,0,wx.CENTER | wx.TOP, 50)
		self.SetSizer(hb1)

	def keyReleased0(self, event):
		self.passText.SetValue(self.passNoText.GetValue())

	def keyReleased1(self, event):
		self.passNoText.SetValue(self.passText.GetValue())

	def newPasswordsTextCtrl(self):
		self.password_shown = False
		self.sizer = wx.BoxSizer(wx.HORIZONTAL)
		self.passText = wx.TextCtrl(self, style=wx.TE_PASSWORD, size=(180, 30))
		self.passNoText = wx.TextCtrl(self, size=(180, 30))
		self.passNoText.Hide()
		self.sizer.Add(self.passText, 0, wx.ALL, 0)
		self.sizer.Add(self.passNoText, 0, wx.ALL, 0)

	def onCheck(self, event):
		self.passText.Show(self.password_shown)
		self.passNoText.Show(not self.password_shown)
		if not self.password_shown:
			self.passNoText.SetValue(self.passText.GetValue())
			self.passNoText.SetFocus()
		else:
			self.passText.SetValue(self.passNoText.GetValue())
			self.passText.SetFocus()
		self.passText.GetParent().Layout()
		self.password_shown = not self.password_shown

		