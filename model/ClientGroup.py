import random,Client 
class ClientGroup:
    
    def __init__(self, clients, eating_time):
        self.clients = clients
        self.eating_time = eating_time

list = []
clientes = random.randint(0,5)
clients = []
for clienteeee in range(clientes):
    clients.append(Client())

for client in clients:
    print(client.table)
    
list.append(ClientGroup(clients, 10))
""" for obj in list:
    print(obj.clients,obj.eating_time,sep = " ") """