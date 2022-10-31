#!/usr/bin/python3

import numpy as np

# Function to calculate I4 for any samples of random variables
def I4(samplearr):
    avg=np.average(samplearr)
    M2=np.sum(np.power(samplearr-np.full(samplearr.shape,avg),2))/samplearr.shape[0]
    M4=np.sum(np.power(samplearr-np.full(samplearr.shape,avg),4))/samplearr.shape[0]
    return M4-3*M2*M2


if __name__=="__main__":
    SampleNo=1000000

# generate random variable x from a normal distribution with average=100, std=3
    mux=100
    sigmax=3
    sizex=SampleNo
    x=np.random.normal(loc=mux,scale=sigmax,size=sizex)

# generate random variable x from a normal distribution with average=200, std=5
    muy=200
    sigmay=7
    sizey=SampleNo
    y=np.random.normal(loc=muy,scale=sigmay,size=sizey)

# get I4's
    I4x=I4(x)
    I4y=I4(y)

# Calculate the summed random variable (X+Y)
    z=np.add(x,y)

    I4z=I4(z)

    print("Semi-variant I4 for X is ",I4x)
    print("Semi-variant I4 for Y is ",I4y)
    print("The sum of semi-variants I4x and I4y is ",I4x+I4y)
    print("The semi-variant I4 for (X+Y) is ",I4z)







