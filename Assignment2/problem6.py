#!/usr/bin/python3

import os
import random
import numpy as np
import math
import matplotlib.pyplot as plt


N=10000
x=np.linspace(0,1,num=N)
A=math.factorial(38)/math.factorial(13)/math.factorial(24)
y=A*np.power(x,13)*np.power(np.subtract(1,x),24)

fig,ax=plt.subplots()
ax.plot(x,y)
ax.set_xlim([0,1])
ax.set_title("normalized posterior distribution")
plt.savefig("posterior.png")

