#!/usr/bin/python3


import numpy as np
import random
import matplotlib.pyplot as plt
import scipy.stats as stats
from problem12 import bootstrap,jacknife

# the following contents are modified from https://stackoverflow.com/a/47762586 and my answer from problem12.py
def parta():
    distributions = [
        {"type": np.random.normal, "kwargs": {"loc": 1, "scale": 2}},
        {"type": np.random.normal, "kwargs": {"loc": 4, "scale": 1}},
    ]
    coefficients = np.array([0.3, 0.7])
    # coefficients /= coefficients.sum()      # in case these did not add up to 1
    num_distr = len(distributions)
    sample_size = 100
    data = np.zeros((sample_size, num_distr))
    # data for invisible distributions
    invisible_size = 10000
    datainvis = np.zeros((invisible_size, num_distr))
    for idx, distr in enumerate(distributions):
        data[:, idx] = distr["type"](size=(sample_size,), **distr["kwargs"])
        datainvis[:, idx] = distr["type"](size=(invisible_size,), **distr["kwargs"])
    random_idx = np.random.choice(np.arange(num_distr), size=(sample_size,), p=coefficients)
    random_idx_invis = np.random.choice(np.arange(num_distr), size=(invisible_size,), p=coefficients)
    sample = data[np.arange(sample_size), random_idx]
    invisible = datainvis[np.arange(invisible_size), random_idx_invis]
    fig,axs=plt.subplots(nrows=1,ncols=3,figsize=(20,10)) 
    axs[0].hist(sample, bins=sample_size)
    axs[1].hist(invisible, bins=300)
    x = np.linspace(-10,10,num=1000)
    axs[2].plot(x, 0.3*stats.norm.pdf(x,loc=1,scale=2)+0.7*stats.norm.pdf(x,loc=4,scale=1))
    axs[2].set_ylim(bottom=0)
    axs[0].set_title("Visible dataset")
    axs[1].set_title("Hidden dataset (population)")
    axs[2].set_title("Actual mixture normal distribution")
    plt.savefig("problem3.png")
    return sample


if __name__=="__main__":
    random.seed(a=None)
    samdata=parta()
    print("______________________Using Bootstrap sampling___________________________")
    bootstrap(samdata,100,200)
    print("______________________Using Jackknife sampling___________________________")
    jacknife(samdata,100)