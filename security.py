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

    def __init__(self,name,password):
        self.name = name
        self.password = password


    def checkState(self,name):
        data = DatabaseConn().cur().execute("SELECT state FROM security WHERE name = '%s'"%name)
        if data.fetchall()[0][0] == "off":
            return True
        else:
            return False


    def changePassword(self):
        if(self.checkState(self.name)):
            conn =  DatabaseConn()
            conn.cur().execute("UPDATE security SET password = '{pass1}' WHERE name = '{name}'".format(pass1 = self.password,name = self.name))
            conn.commit()
            conn.close()
            return True
        else:
            return False


    def addAccount(self,status):
        conn = DatabaseConn()
        conn.cur().execute("INSERT INTO security (name,password,status,state) VALUES ('{name1}','{pass1}','{status1}','{state1}')".format(name1 = self.name,pass1 = self.password,status1=status,state1='off'))
        conn.commit()
        conn.close()

    def deleteAccount(self):
        conn = DatabaseConn()
        conn.cur().execute("DELETE FROM security WHERE name = '{name1}'".format(name1=self.name))
        conn.commit()
        conn.close()






