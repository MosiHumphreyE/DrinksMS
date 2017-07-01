#!/user/bin/python

from security import AccountManager

manager = AccountManager()
print manager.getOldPassword('admin')[0][0]
