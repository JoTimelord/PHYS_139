#!/usr/bin/python3

import os
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.pyplot import cm

random.seed(a=None)

sequence=[1,2,3,4,5,6]

# Number of maximum dices
N=10000
n=np.arange(0,N+1,step=50,dtype=int)
AVG=np.zeros(n.shape)


index=0
# Increment the number of dices
for Ntrial in n:
    if Ntrial!=0:
    # Get value of each dice
        VALS=random.choices(sequence,k=Ntrial)
        AVG[index]=sum(VALS)/len(VALS)
        index+=1

# plot average as a function of n dices
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(n, AVG, color='tab:blue')
ax.set_xlim([0, N+1])
ax.set_ylim([2, 5])
ax.set_title('Average value of N dices as a function of N')
plt.savefig("Dicethrow1.png")

# Prove central limit theorem in the distribution of Xn
trial=1000

fig,ax=plt.subplots()


step=1000
color = cm.rainbow(np.linspace(0, 1, int(N/step)))
c=0
for Ntrial in n:
    if Ntrial%step==0 and Ntrial>0:
        print (Ntrial)
        AVGARR=np.zeros(trial)
        for i in range(trial):
            VALS=random.choices(sequence,k=Ntrial)
            AVGARR[i]=sum(VALS)/len(VALS)
        counts,bin_edges=np.histogram(AVGARR,bins=100)
        counts2,bin_edges2=np.histogram(AVGARR,bins=100,density=True)
        probability=counts/float(counts.sum())
        name="N="+str(Ntrial)
        bins=(bin_edges[:-1]+bin_edges[1:])/2
        bins2=(bin_edges2[:-1]+bin_edges2[1:])/2
# plot distribution curves
        ax.plot(bins,probability,label=name,c=color[c])
        #ax.plot(bins2,counts2,label=name,c=color[c])
        c+=1

ax.set_xlabel(r"$X_n$: Average of n samples")
ax.set_ylabel(r"Probability mass function")
#ax.set_ylabel("Probability density function")
ax.set_title("Central limit theorem")
ax.legend()
plt.savefig("CLT.png")
#plt.savefig("PDF.png")













