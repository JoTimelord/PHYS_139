#!/usr/bin/python3

import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

filename="data_2022oct30.txt"

# use numpy to extract the data columns
x=np.loadtxt(filename,skiprows=0,usecols=0)
y=np.loadtxt(filename,skiprows=0,usecols=1)
e=np.loadtxt(filename,skiprows=0,usecols=2)

# plot the graph in Part A
plt.figure()
plt.errorbar(x,y,yerr=e,fmt='o')
plt.xlim(right=8)
plt.ylim(bottom=0)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("XY data with errors on Y")
plt.savefig("parta.png")

# use scipy to fit the function for Part B
def bmodel(x,b1,b2,b3,b4,b5):
    f=b1*np.exp(-b2*x)+b3*np.exp(-1/2*(x-b4)*(x-b4)/b5/b5)
    return f

parameters,covariance=curve_fit(bmodel,x,y)








