#!/usr/bin/python3

import os
import random
import argparse

if __name__=="__main__":
    random.seed(a=None)

    sequence=[1,2,3,4,7,8,9]
    Ntrials=200000

    print(Ntrials," trials are conducted. \n")

    eight=0

    for i in range(0,Ntrials):
        val1=random.choice(sequence)
        val2=random.choice(sequence)
        if val1+val2==8:
            eight+=1
    print(eight," trials returned a sum of 8. \n")
    print("The probability of producing a sum of eight is ", eight/Ntrials, "\n")


