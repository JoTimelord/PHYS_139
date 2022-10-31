#!/usr/bin/python3

import numpy as np
import os
import random
from problem5 import I4

# Draw a list of random variables from the following sequence
xseq=[1,2,3,4,5,6,7]
yseq=[100,101,102,103,104,105,106,107,108]
N=100000
x=np.asarray(random.choices(xseq,k=N))
y=np.asarray(random.choices(yseq,k=N))
z=np.add(x,y)

I4x=I4(x)
I4y=I4(y)
I4z=I4(z)

print("Semi-variant I4 for X is ",I4x)
print("Semi-variant I4 for Y is ",I4y)
print("The sum of semi-variants I4x and I4y is ",I4x+I4y)
print("The semi-variant I4 for (X+Y) is ",I4z)



