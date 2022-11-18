#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import random

def parta():
    # draw 100 data points as sample
    data=np.random.gamma(4,1,size=100)
    print("The mean of the sample with size of 100 is: ",np.average(data))
    print("The variance of the sample is: ", np.var(data))
    fig,axs=plt.subplots(nrows=1,ncols=3,figsize=(20,10))
    axs[0].hist(data,bins=100)
    axs[0].set_title("Visible dataset")
    # draw 100000 data from the distribution as hidden side
    data2=np.random.gamma(4,1,size=100000)
    axs[1].hist(data2,bins=1000)
    axs[1].set_title("Hidden dataset (population)")
    # use analytical form of the gamma function to plot the curve
    x=np.linspace(0,20,200)
    y=stats.gamma.pdf(x,a=4,scale=1)
    axs[2].plot(x,y)
    axs[2].set_xlim(left=0)
    axs[2].set_ylim(bottom=0)
    axs[2].set_title("Actual Gamma(4,1) function")
    plt.savefig("problem1a.png")
    return data

def bootstrap(inputdata,n,samplesize):
    ratio=np.zeros(n)
    for i in range(0,n):
        boot=random.choices(inputdata,k=samplesize)
        median=np.median(boot)
        mean=np.average(boot)
        ratio[i]=mean/median
    error=np.std(ratio,ddof=1)
    average=np.average(ratio)
    print("The average ratio of mean over median is ", average)
    print("The standard error in ratio of mean over median is ", error)

# for sampling in invisible distribution
def partb(n):
    ratio=np.zeros(n)
    for i in range(0,n):
        data=np.random.gamma(4,1,size=100)
        median=np.median(data)
        mean=np.average(data)
        ratio[i]=mean/median
    print("The average ratio of mean over median is ",np.average(ratio))
    print("The standard error of mean over median is ",np.std(ratio,ddof=1))    

# jacknife methods which takes in the sample distribution and produce n jackknife samples
def jacknife(inputdata,n):
    ratio=np.zeros(n)
    for i in range(0,n):
        data=np.delete(inputdata,random.randrange(0,100))
        median=np.median(data)
        mean=np.average(data)
        ratio[i]=mean/median
    print("The average ratio of mean over median is ",np.average(ratio))
    print("The standard error of mean over median is ",np.sqrt((np.var(ratio))*(n-1)))  


if __name__=="__main__":
    random.seed(a=None)
    samdata=parta()
    print("======================Problem 1======================")
    print("______________________Using Bootstrap sampling___________________________")
    bootstrap(samdata,100,200)
    print("______________________________________________________________________________________")
    print("______________________Using Invisible distribution sampling___________________________")
    partb(100)
    print("======================Problem 2======================")
    print("______________________Using Jackknife sampling___________________________")
    jacknife(samdata,100)
    print("______________________________________________________________________________________")
    print("______________________Using Invisible distribution sampling___________________________")
    partb(100)
    