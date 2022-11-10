#!/usr/bin/python3

import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import scipy.stats as st
from scipy.stats import multivariate_normal

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
    chi2=np.sum(np.power(np.divide(np.subtract(y,expecty),e),2))
    return chi2


# borrow the useful function unit from David's solution
def unit(i):
    return (np.arange(5)==i).astype(int)

hessian=np.zeros(shape=(5,5))
h=0.0001
b0params=np.asarray([fitb1,fitb2,fitb3,fitb4,fitb5])

# Part G: Goodness-of-fit
print("The chi squared value for the best fit is: ")
print(chisqr(b0params))
print("This has a p-value of ", st.chi2.sf(x=chisqr(b0params),df=23-5))

print ("These are the values of the best fit: ")
print (b0params)
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
cov=np.linalg.inv(1/2*hessian)
print("The covariance matrix is ")
print(cov)

# Part D: Confidence Interval
print("The 90% confidence interval is ")
print(st.norm.interval(confidence=0.9,loc=fitb1,scale=np.sqrt(cov[0,0])))
print("The 68% confidence interval is ")
print(st.norm.interval(confidence=0.68,loc=fitb1,scale=np.sqrt(cov[0,0])))

print("calculated by scipy package covariance")
print("The 90% confidence interval is ")
print(st.norm.interval(confidence=0.9,loc=fitb1,scale=np.sqrt(covariance[0,0])))
print("The 68% confidence interval is ")
print(st.norm.interval(confidence=0.68,loc=fitb1,scale=np.sqrt(covariance[0,0])))

# Part E: Contour plot
def rho(covmatrix,b3,b5):
    determinant=covmatrix[2,2]*covmatrix[4,4]-covmatrix[2,4]*covmatrix[4,2]
    constant=1/np.sqrt(np.power(2*np.pi,2)*determinant)
    b3b5=np.asarray([b3-fitb3,b5-fitb5])
    factor=np.exp(-1/2*np.linalg.dot(np.linalg.matmul(b3b5,np.asarray(cov35)),b3b5))
    return factor*constant

# We notice that this is multivariate normal
cov35=[[cov[2,2],cov[2,4]],[cov[4,2],cov[4,4]]]
x, y = np.mgrid[0.75:1.5:.005, 1.3:2.5:.005]
rv = multivariate_normal([fitb3, fitb5],cov35)
data = np.dstack((x, y))
z = rv.pdf(data)
plt.figure()
plt.contourf(x, y, z, levels=[0.5,0.9,0.95], cmap='coolwarm')
plt.xlabel("b3")
plt.ylabel("b5")
plt.title("confidence level at 0.5 and 0.9 and 0.95")
plt.savefig("partd.png")








