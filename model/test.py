import random as ran

from Kitchen import Kitchen as k
from Order import Order as o

import numpy as np

#importing and creating object test
#cocina = k(name='cocina 1')#
from model.Customer import Customer
from model.CustomerGroup import CustomerGroup
from model.Table import Table

from model.Cashier import Cashier
from model.Order import Order
from model.Plate import Plate


plate= Plate("Churrasco", 5, 15, 80, 4,1)
plateTwo= Plate("Bistec a Caballo", 5, 10, 2, 4,2)
plateThree= Plate("Frijoles con Cayo", 5, 5, 2, 4,1)
plateList1=[plate,plateTwo]
plateList2=[plate,plateTwo,plateThree]
plateList3=[plate]

order1=Order(1,plateList1)
order2=Order(2,plateList2)
order3=Order(3,plateList3)


# Creacion de mesas
mesasList=[]
for i in range(20):
   mesasList.append(Table(i+1))






# Creacion listas con clientes
customerGroupList=[]
for i in range (ran.randint(1,5)):
   tip=ran.randint(0,1)
   share = 0
   if tip==1:
      tip=True
      share = False
   else:
      tip=False
      share = True
   # print(tip)
   customer=Customer(ran.randint(1,1000),tip, 4, share)
   customerGroupList.append(customer)


# Creacion de grupos
customerGroup = CustomerGroup(1, customerGroupList, ran.randint(1, 3), ran.randint(1, 3))
customerGroup2 = CustomerGroup(2, customerGroupList, ran.randint(1, 3), ran.randint(1, 3))
customerGroup3 = CustomerGroup(3, customerGroupList, ran.randint(1, 3), ran.randint(1, 3))
customerGroup4 = CustomerGroup(4, customerGroupList, ran.randint(1, 3), ran.randint(1, 3))

# for i in range(len(mesasList)):
#    if mesasList[i].tableAvailable() and (len(mesasList[i].customersGroupList[0].customer)+len(customerGroup.customer)<=5):

mesasList[0].addCustomer(customerGroup)
mesasList[0].addCustomer(customerGroup2)
mesasList[0].show()

print(mesasList[0].tableAvailable())


for i in range(len(customerGroupList)):
   cuentaOrder=ran.randint(1,3)
   if cuentaOrder==1 :
      customerGroupList[i].order=order1
   elif cuentaOrder==2 :
      customerGroupList[i].order=order2
   else :
      customerGroupList[i].order=order3



# Muestra informacion
for i in range(len(customerGroup.customer)):
   print(customerGroup.customer[i].customer_id)
   for j in range(len(customerGroup.customer[i].order.plates)):
      print(customerGroup.customer[i].order.plates[j].name)




cashier= Cashier()

cashier.addClientGropQueue(customerGroup)
cashier.addClientGropQueue(customerGroup2)
cashier.addClientGropQueue(customerGroup3)
cashier.addClientGropQueue(customerGroup4)

cashier.start()
# cashier.totalPay()




















































# listaPrueba=np.array(customerGroup)

# trueCounter = 0
# for i in range(listaPrueba.size):
#    if listaPrueba[i]:
#       trueCounter += 1
# print(listaPrueba[0].)

# print(listaPrueba)
# mesa=Table(False, 1)
# mesa.addCustomer(customerGroup)
# print(mesa.mostrar())
#print("ff")

# mesa=Table(False, 1)
# mesa.addCustomer(customerGroup)
# mesa.addCustomer(customerGroup2)
# print("ID cliente", mesa.show())


#
# lol = o('holsd','dsa')
# lol1 = o('holsd','dsa')
# lol2 = o('holsd','dsa')
#
# j = [lol, lol1, lol2]
#
# k = np.array(j)





