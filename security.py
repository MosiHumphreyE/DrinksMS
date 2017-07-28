#!/user/bin/python

from databaseConn import DatabaseConn

class Security:

    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.status = "login"
        self.state = "out"
        self.access = False

    def checkpass(self,cur):
        for row in cur:
            if (row[0]==self.name) & (row[1]==self.password):
                self.access = True
                self.status = row[2]
                self.state = "in"
                break
        return self.access

    def getStatus(self):
        return self.status

    def getState(self):
        return self.state



class AccountManager:

    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.conn = DatabaseConn()


    def __init__(self):
        self.conn = DatabaseConn()

    def setName(self,name):
        self.name = name

    def setPassword(self, password):
            self.password = password

    def getName(self):
            return self.name

    def getPassword(self):
            return self.password

    def checkState(self,name):
        data = self.conn.cur().execute("SELECT state FROM security WHERE name = '%s'"%name)
        if data.fetchall()[0][0] == "off":
            return True
        else:
            return False


    def changePassword(self):
        if(self.checkState(self.name)):
            self.conn.cur().execute("UPDATE security SET password = '{pass1}' WHERE name = '{name}'".format(pass1 = self.password,name = self.name))
            self.conn.commit()
            self.conn.close()
            return True
        else:
            return False


    def addAccount(self,status):
        self.conn.cur().execute("INSERT INTO security (name,password,status,state) VALUES ('{name1}','{pass1}','{status1}','{state1}')".format(name1 = self.name,pass1 = self.password,status1=status,state1='off'))
        self.conn.commit()
        self.conn.close()

    def deleteAccount(self):
        self.conn.cur().execute("DELETE FROM security WHERE name = '{name1}'".format(name1=self.name))
        self.conn.commit()

    def getLoginAcc(self):
        cur = self.conn.cur().execute("SELECT password, status FROM security WHERE state = 'on'")
        items = []
        for row in cur:
            items.append(row[0])
        return items

    def getUserNames(self):
        return self.conn.cur().execute("SELECT name FROM security WHERE state = 'off'")

    def getOldPassword(self,name):
        password = []
        for row in self.conn.cur().execute("SELECT password FROM security WHERE name = '{name1}'".format(name1=name)):
            password.append(row)
        return password

