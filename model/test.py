import random as ran

from Kitchen import Kitchen as k
from Order import Order as o

import numpy as np

from Kitchen import Kitchen as k


#importing and creating object test
#cocina = k(name='cocina 1')#
from Customer import Customer
from CustomerGroup import CustomerGroup
from Table import Table

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
mesa.addCustomer(customerGroup._get_customer())
print("ID cliente", mesa.mostrar())



lol = o('holsd','dsa')
lol1 = o('holsd','dsa')
lol2 = o('holsd','dsa')

j = [lol, lol1, lol2]

k = np.array(j)





