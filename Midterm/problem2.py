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
def bmodel(xdata,b1,b2,b3,b4,b5):
    f=b1*np.exp(-b2*xdata)+b3*np.exp(-1/2*(xdata-b4)*(xdata-b4)/b5/b5)
    return f

parameters,covariance=curve_fit(bmodel,x,y,sigma=e)
fitb1=parameters[0]
fitb2=parameters[1]
fitb3=parameters[2]
fitb4=parameters[3]
fitb5=parameters[4]

print("The covariance matrix calculated by scipy package:")
print(covariance)

# use the fit parameters to draw the fitted function
plt.figure()
plt.errorbar(x,y,yerr=e,fmt='o',label='data')
fity=bmodel(x,fitb1,fitb2,fitb3,fitb4,fitb5)
plt.plot(x,fity,'-',label='fit')
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.title("XY data with fitted line")
plt.savefig("partb.png")


# PART C
# define chisqr function
def chisqr(blist):
    expecty=bmodel(x,blist[0],blist[1],blist[2],blist[3],blist[4])
    chi2=np.sum(np.divide(np.subtract(y,expecty),e))
    return chi2

# borrow the useful function unit from David's solution
def unit(i):
    return (np.arange(5)==i).astype(int)

hessian=np.zeros(shape=(5,5))
h=0.001
b0params=np.asarray([fitb1,fitb2,fitb3,fitb4,fitb5])
for i in range(0,5):
    for j in range(0,5):
        fpp=chisqr(b0params+h*unit(i)+h*unit(j))
        fpm=chisqr(b0params+h*unit(i)-h*unit(j))
        fmp=chisqr(b0params-h*unit(i)+h*unit(j))
        fmm=chisqr(b0params-h*unit(i)-h*unit(j))
        hessian[i,j]=(fpp+fmm-fpm-fmp)/(4*np.power(h,2))

print("The hessian matrix calculated: ")
print(hessian)

# compute covariance matrix
cov=np.linalg.inv(0.5*hessian)
print("The covariance matrix is ")
print(cov)

# Part D
















