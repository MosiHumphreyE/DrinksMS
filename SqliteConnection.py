import wx
from databaseConn import DatabaseConn
from security import Security
# conn2DB = sqlite3.connect("drinksDB.db")
# cur = conn2DB.cursor();
# # cur.execute("CREATE  TABLE mainStock(indexNo INTEGER PRIMARY KEY  AUTOINCREMENT  NOT NULL ,"
# #               "name TEXT NOT NULL , quantity DOUBLE NOT NULL , date DATETIME NOT NULL "
# #               " DEFAULT CURRENT_DATE)")
# print "trying"
# cur.execute("insert into mainStock (name,quantity) values(?,?);",('pepsi',11.0))
# conn2DB.commit()
# print "First trail finished"
# conn2DB.close()
# print "Openning connection to the database"
# con = DatabaseConn()
# cur = con.cur()
# cur.execute("insert into mainStock (name,quantity) values(?,?);", ('masele', 1.0))
# con.commit()
# con.close()
# print "we are done closing"

testing = Security("masele","kimada")
con = DatabaseConn()
cur = con.cur()
results = cur.execute("select name,password,status,state from security")
ans = testing.checkpass(results)
print ans