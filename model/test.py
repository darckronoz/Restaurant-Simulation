import random as ran

from Kitchen import Kitchen as k
from Order import Order as o

import numpy as np

#importing and creating object test
#cocina = k(name='cocina 1')#
from Customer import Customer
from CustomerGroup import CustomerGroup
from Table import Table

from model.Order import Order
from model.Plate import Plate

plate= Plate("Churrasco", 5, 20, 2, 4,1)
plateTwo= Plate("Papa Salada", 5, 20, 2, 4,2)
plateThree= Plate("Yuca", 5, 20, 2, 4,1)
plateList=[plate,plateTwo,plateThree]

order=Order(1,plateList)

customerList=[]
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
   customerList.append(customer)


customerGroup=CustomerGroup(customerList, ran.randint(1,3),ran.randint(1,3))
customerGroup2=CustomerGroup(customerList, ran.randint(1,3),ran.randint(1,3))


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

mesa=Table(False, 1)
mesa.addCustomer(customerGroup)
# mesa.addCustomer(customerGroup2)
print("ID cliente", mesa.show())


#
# lol = o('holsd','dsa')
# lol1 = o('holsd','dsa')
# lol2 = o('holsd','dsa')
#
# j = [lol, lol1, lol2]
#
# k = np.array(j)





