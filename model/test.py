import random as ran

from Kitchen import Kitchen as k
from Order import Order as o

import numpy as np

#importing and creating object test
#cocina = k(name='cocina 1')#
from Customer import Customer
from CustomerGroup import CustomerGroup
from Table import Table

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

for i in range(len(customerGroupList)):
   cuentaOrder=ran.randint(1,3)
   if cuentaOrder==1 :
      customerGroupList[i].order=order1
   elif cuentaOrder==2 :
      customerGroupList[i].order=order2
   else :
      customerGroupList[i].order=order3
customerGroup=CustomerGroup(customerGroupList, ran.randint(1, 3), ran.randint(1, 3))
customerGroup2=CustomerGroup(customerGroupList, ran.randint(1, 3), ran.randint(1, 3))

for i in range(len(customerGroup.customer)):
   print(customerGroup.customer[i].customer_id)
   for j in range(len(customerGroup.customer[i].order.plates)):
      print(customerGroup.customer[i].order.plates[j].name)


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


cashier= Cashier()
cashier.addClientGropQueue(customerGroup)
# print("Total", cashier.payBill())
cashier.totalPay()

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





