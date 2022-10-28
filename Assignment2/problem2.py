#!/usr/bin/python3

import random
import os

N=1000000000
INCLUSIVE=0

random.seed(a=None)

for i in range(0,N):
    HEADS=0
    for i in range(0,N):
        value=random.random()
        if value<=0.5:
            HEADS+=1
    if HEADS<=500200000 and HEADS>=500100000:
        INCLUSIVE+=1

print ("The probability of the number of heads between 500,100,000 and 500,200,000 is ", INCLUSIVE/N)



