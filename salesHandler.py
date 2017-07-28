#!/user/bin/python

from databaseConn import DatabaseConn


class SalesHandler:


    def __init__(self):
        self.connect = DatabaseConn()


    def lists(self):
        values = self.connect.cur().execute("select name from mainStock where quantity  > 0")
        list = []
        for row in values:
            list.append(row)
        return list


class Sales:

    def __init__(self,name,amount):
        self.name = name
        self.amount = amount
        self.connect = DatabaseConn()

    def getName(self):
        return self.name

    def getCost(self):
        results = self.connect.cur().execute("SELECT  saleCost FROM mainStock WHERE name = '{name}'".format(name=self.name))
        for row in results:
            cost =int(row[0])
        return cost

    def getAmount(self):
        return self.amount

    def getTotalCost(self):
        return str(int(self.getCost())*int(self.amount))