#!/usr/bin/python3

import os
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

random.seed(a=None)

sequence=[1,2,3,4,5,6]

N=1000000
n=np.linspace(0,N,retstep=5)
AVG=np.zeros(n.shape)

index=0
for Ntrial in n:
    for i in range(Ntrial):
        AVG[index]+=random.choice(sequence)/Ntrial
    if Ntrial%100==0:

    index+=1

# plot average as a function of n dices
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(xdata1, ydata1, color='tab:blue')
ax.set_xlim([0, N+1])
ax.set_ylim([0, 6])
ax.set_title('Average value of N dices as a function of N')
plt.savefig("Dicethrow1.png")

# plot distribution curves









