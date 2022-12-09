#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import random

# The following function is adapted from: https://stackoverflow.com/a/55737551 
def multivariate_gaussian(pos, mu, Sigma):
    """Return the multivariate Gaussian distribution on array pos."""

    n = mu.shape[0]
    Sigma_det = np.linalg.det(Sigma)
    Sigma_inv = np.linalg.inv(Sigma)
    N = np.sqrt((2*np.pi)**n * Sigma_det)
    # This einsum call calculates (x-mu)T.Sigma-1.(x-mu) in a vectorized
    # way across all the input variables.
    fac = np.einsum('...k,kl,...l->...', pos-mu, Sigma_inv, pos-mu)

    return np.exp(-fac / 2) / N

def metropolis(N,init1,init2):
    x1samples = np.zeros(N)
    x2samples = np.zeros(N)
    # Choose initial values of x1, x2
    x1curr = init1
    x2curr = init2
    filled = 0
    while filled < N:
        # generate next candidate points based on a normal distribution
        x1proposed = np.random.normal(loc=x1curr,scale=2)
        x2proposed = np.random.normal(loc=x2curr,scale=2)
        # calculate acceptance
        covariance = [[0.25,0],[0,2]]
        pcurr = 0.5*stats.multivariate_normal.pdf([x1curr,x2curr],mean=[0,0],cov=covariance)
        pcurr += 0.5*stats.multivariate_normal.pdf([x1curr,x2curr],mean=[5,5],cov=covariance)
        pproposed = 0.5*stats.multivariate_normal.pdf([x1proposed,x2proposed],mean=[0,0],cov=covariance)
        pproposed += 0.5*stats.multivariate_normal.pdf([x1proposed,x2proposed],mean=[5,5],cov=covariance)
        if pproposed >= pcurr:
            x1curr = x1proposed
            x2curr = x2proposed
            x1samples[filled]=x1curr
            x2samples[filled]=x2curr
            filled+=1
        else:
            u = random.random()
            if u <= pproposed/pcurr:
                x1curr = x1proposed
                x2curr = x2proposed
                x1samples[filled]=x1curr
                x2samples[filled]=x2curr
                filled+=1
            else:
                x1samples[filled]=x1curr
                x2samples[filled]=x2curr
                filled+=1
    return x1samples,x2samples


def plot2d():
    # Our 2-dimensional distribution will be over variables X and Y
    N = 1000
    X = np.linspace(-7, 10, N)
    Y = np.linspace(-7, 10, N)
    X, Y = np.meshgrid(X, Y)

    # Mean vector and covariance matrix
    mu1 = np.array([0., 0.])
    Sigma1 = np.array([[ 0.25 , 0.], [0.,  2]])
    mu2=np.array([5, 5])
    Sigma2= Sigma1

    # Pack X and Y into a single 3-dimensional array
    pos = np.empty(X.shape + (2,))
    pos[:, :, 0] = X
    pos[:, :, 1] = Y

    # call the two multivariate gaussians
    Z1=multivariate_gaussian(pos, mu1, Sigma1)
    Z2=multivariate_gaussian(pos, mu2, Sigma2)
    
    Z=0.5*Z1+0.5*Z2

    # plot using subplots
    fig = plt.figure(figsize=(15,10))
    ax = plt.axes(projection='3d')
    # ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
    #            cmap='viridis', edgecolor='none')
    ax.contour3D(X, Y, Z, 50, cmap='binary')
    ax.set_xlabel(r'$x_1$')
    ax.set_ylabel(r'$x_2$')
    ax.set_zlabel('z')
    ax.set_title('probability density function')

    plt.savefig('problem1a.png')

if __name__=="__main__":
    # plot2d()
    x1,x2=metropolis(10000,0,0)
    # n = np.linspace(0,100000,num=100000)
    # fig = plt.figure()
    # plt.plot(n,x1)
    # plt.title("Change of x1 over sampling time")
    # plt.ylabel(r'x_1')
    # plt.savefig("x1.png")
    print ("The mean value of (x1,x2) is ", (np.mean(x1), np.mean(x2)))
    # 3D histogram modified from https://matplotlib.org/stable/gallery/mplot3d/hist3d.html
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    hist, xedges, yedges = np.histogram2d(x1, x2)

    # Construct arrays for the anchor positions of the bars
    xpos, ypos = np.meshgrid(xedges[:-1], yedges[:-1], indexing="ij")
    xpos = xpos.ravel()
    ypos = ypos.ravel()
    zpos = 0

    # Construct arrays with the dimensions for the 16 bars.
    dx = dy = 0.5 * np.ones_like(zpos)
    dz = hist.ravel()

    ax.bar3d(xpos, ypos, zpos, dx, dy, dz, zsort='average')
    ax.set_xlabel(r'$x_1$')
    ax.set_ylabel(r'$x_2$')
    ax.set_zlabel('raw count')
    plt.savefig('3Dhist.png')
