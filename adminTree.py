import wx


class AdminTree(wx.Panel):
    def __init__(self,parent,id):
        wx.Panel.__init__(self,parent,id,style=wx.BORDER_SUNKEN)
        tree = wx.TreeCtrl(self)
        tree.SetSize((220,900))
        admin = tree.AddRoot("Administrator")
        addStock = tree.AppendItem(admin,"Add stock")
        updateStock = tree.AppendItem(admin, "Update stock")
        viewReport = tree.AppendItem(admin,"View report")
        salesReport = tree.AppendItem(viewReport,"Sales report")
        scurrentStock =  tree.AppendItem(viewReport,"Available stock report")
        addStock = tree.AppendItem(viewReport,"Added stock report")
        accountManagement = tree.AppendItem(admin,"Edit account")
        createAccount = tree.AppendItem(accountManagement,"Create account")
        changePassword = tree.AppendItem(accountManagement,"Change password")
        deleteAccount = tree.AppendItem(accountManagement,"Delete Account")
        closeSales =  tree.AppendItem(admin,"End Sales")
        tree.Expand(admin)

