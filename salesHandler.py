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
