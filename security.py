#!/user/bin/python


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