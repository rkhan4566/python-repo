#importing modules in python : modules and pacakages
#In python modules and packages help organise and reuse code.here a comprehensive guide on how to import them.
import math
result=math.sqrt(25)
print(result)

from math import sqrt,pi
print(sqrt(25))
print(sqrt(49))
print(pi)

import numpy as np
result=np.array([1,2,3,4,5])
print(result)

from math import *
result1=sqrt(25)
print(result1)

from package.maths import addition
result=addition(2,4)
print(result)

from package.maths import substraction
result=substraction(4,2)
print(result)

from package.maths import multiplication
result=multiplication(4,2)
print(result)