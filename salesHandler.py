#!/user/bin/python

from databaseConn import DatabaseConn


class SalesHandler:


    def __init__(self):
        self.connect = DatabaseConn()


    def lists(self):
        values = self.connect.cur().execute("select name from mainStock")
        list = []
        for row in values:
            list.append(row)
        return list


class Sales:

    def __init__(self,name,amount):
        self.name = name
        self.amount = amount
        self.connect = DatabaseConn()
        self.cost = self.getCostPerDrint()

    def getCostPerDrint(self):
        data = self.connect.cur().execute("SELECT costperdrink FROM mainStock WHERE name = '{name}'".
                                          format(name=self.name))
        cost = ''
        for row in data:
            cost = row[0]

        return cost

    def getName(self):
        return self.name

    def getAmount(self):
        return self.amount

    def getCost(self):
        return self.cost

    def getTotalCost(self):
        return str(int(self.cost)*int(self.amount))