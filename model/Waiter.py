
class Waiter:

    # waiter_id: unique waiter id.
    # state: True if Ocuped, False if Free.
    # order_time: time that takes the waiter to take an order.
    # clean _time: time that takes the waiter to clean a table.
    # service_time: array with the times that takes to the waiter to bring the plate from the kitchen to the table**
    # the positions of the array change depending on the zone of tables that the waiter is attending.
    # tables: array with the tables.
    # tips: tips counter, acumulates all the tip the waiter has recieved
    # score: averages the score the waiter has received
    def __init__(self, waiter_id, state, order_time, clean_time, service_time, tables, tips, score):
        self.waiter_id = waiter_id
        self.state = state
        self.order_time = order_time
        self.clean_time = clean_time
        self.service_time = service_time
        self.tables = tables
        self.tips = tips
        self.score = score

    # this function assigns customers to tables and if all the tables are full
    # then adds the customer to the tableQueue
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
    
    # Function that returns the first empty table on the table list (self.tables)
    # if there's not empty tables returns False.
    def findEmptyTable(self):
        for table in self.tables:
            if table.isEmpty():
                return table.id
        return False

    # function that returns the first shareable table on the list
    # if the table is shareable but the group doesn't fit it isnt returned
    # if there are not tables to share that meet the requirements (have enough space to the client group)
    # returns False
    def findTableToShare(self, groupLenght):
        for table in self.tables:
            if table.shareable: 
                if table.getFreeSeats() <= groupLenght:
                    return table.id
        return False




