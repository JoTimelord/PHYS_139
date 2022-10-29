#!/usr/bin/python3

import numpy as np

# generate random variable x from a normal distribution with average=50, std=5
mux=50
sigmax=5
sizex=10000
x=random.normal(loc=mux,scale=sigmax,size=sizex)

# generate random variable x from a normal distribution with average=100, std=20
muy=100
sigmay=20
sizey=10000
y=random.normal(loc=muy,scale=sigmay,size=sizey)

# Calculate the average of the data points drawn from the distribution
avgx=np.average(x)
avgy=np.average(y)

# Calculate the individual semi-invariant I4
I4x=np.power(x-np.full(x.shape,avgx),4)/sizex
I4y=np.sum(np.power(y-np.full(y.shape,avgy),4))/sizey

I4tot=np.






