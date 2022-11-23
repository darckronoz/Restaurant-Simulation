import random as ran
from Kitchen import Kitchen as k
import numpy as np

#importing and creating object test
#cocina = k(name='cocina 1')#
from model.Customer import Customer
from model.CustomerGroup import CustomerGroup
from model.Table import Table

customerList=[]
for i in range (ran.randint(1,5)):
   tip=ran.randint(0,1)
   if tip==1:
      tip=True
   else:
      tip=False
   # print(tip)
   customer=Customer(1,tip, 4 )
   customerList.append(customer)

customerGroup=CustomerGroup(customerList, ran.randint(1,3),ran.randint(1,3))
# mesa=Table(False, 1)
# mesa.addCustomer(customerGroup)
# print(mesa.mostrar())



