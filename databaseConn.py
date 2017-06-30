#!/user/bin/python

import sqlite3



class DatabaseConn:

    def __init__(self):
        self.databaseConnection = sqlite3.connect("drinksData.db")

    def commit(self):
        self.databaseConnection.commit()

    def close(self):
        self.databaseConnection.close()

    def cur(self):
        return self.databaseConnection.cursor()

