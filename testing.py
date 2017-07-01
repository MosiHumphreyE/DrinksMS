from salesHandler import SalesHandler

sale = SalesHandler()
i = 0
for row in sale.lists():
    print row[i]
    ++i