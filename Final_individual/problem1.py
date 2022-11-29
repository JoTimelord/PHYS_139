#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

# The following function is adapted from: https://stackoverflow.com/a/55737551 
def plot2d():
    # Our 2-dimensional distribution will be over variables X and Y
    N = 1000
    X = np.linspace(-15, 15, N)
    Y = np.linspace(-15, 15, N)
    X, Y = np.meshgrid(X, Y)

    # Mean vector and covariance matrix
    mu = np.array([0., 0.])
    Sigma = np.array([[ 1. , -0.5], [-0.5,  1.]])

    # Pack X and Y into a single 3-dimensional array
    pos = np.empty(X.shape + (2,))
    pos[:, :, 0] = X
    pos[:, :, 1] = Y

    # plot using subplots
    fig = plt.figure()
    ax1 = fig.add_subplot(2,1,1,projection='3d')
    ax1.plot_surface(X, Y, Z, rstride=3, cstride=3, linewidth=1, antialiased=True,
                cmap=cm.viridis)
    ax1.view_init(55,-70)
    ax1.set_xticks([])
    ax1.set_yticks([])
    ax1.set_zticks([])
    ax1.set_xlabel(r'$x_1$')
    ax1.set_ylabel(r'$x_2$')

    ax2 = fig.add_subplot(2,1,2,projection='3d')
    ax2.contourf(X, Y, Z, zdir='z', offset=0, cmap=cm.viridis)
    ax2.view_init(90, 270)

    ax2.grid(False)
    ax2.set_xticks([])
    ax2.set_yticks([])
    ax2.set_zticks([])
    ax2.set_xlabel(r'$x_1$')
    ax2.set_ylabel(r'$x_2$')

    plt.show()

