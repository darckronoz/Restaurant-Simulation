
class Waiter:

    def __init__(self, waiter_id, state, order_time, clean_time, service_time, tables, tips, score):
        self.waiter_id = waiter_id
        self.state = state
        self.order_time = order_time
        self.clean_time = clean_time
        self.service_time = service_time
        self.tables = tables
        self.tips = tips
        self.score = score

    #this function assigns customers to tables and if all the tables are full
    #then adds the customer to the tableQueue
    def assignTable(self, customers, tableQueue):
        table = self.findEmptyTable()
        if table != False:
            self.tables[table].addCustomer(customers)
        else:
            table = self.findTableToShare(customers.getSize())
            if table != False:
                self.tables[table].addCustomer(customers)
            else:
                tableQueue.push(customers)
    
    #Function that returns the first empty table on the table list (self.tables)
    #if there's not empty tables returns False.
    def findEmptyTable(self):
        for table in self.tables:
            if table.isEmpty() == True:
                return table.id
        return False

    #function that returns the first shareable table on the list
    #if the table is shareable but the group doesn't fit it isnt returned
    #if there are not tables to share that meet the requirements (have enough space to the client group)
    #returns False
    def findTableToShare(self, groupLenght):
        for table in self.tables:
            if table.shareable: 
                if table.getFreeSeats() <= groupLenght:
                    return table.id
        return False




