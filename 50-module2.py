# note please rename file 49-module as module11

# get data from the module1 file 

import module1 

print(module1.sum(2,3))


# another method is 
import module1 as mod

print(mod.mul(2,3))


# if you want use only one specific function  
from module1 import mul

print(mul(2,2))


# if you want to use all function
from module1 import *

print(sum(4,2))
print(mul(4,2))

