#!/usr/bin/python3

import os
import random
import argparse



if __name__=="__main__":
    random.seed(a=None)
    print("Does god throw dice?")

    Ntrials=10000
    YES1=0
    YES2=0

# probability of 1/4
    value=random.random()
    if value<=0.5:
        if random.random()<=0.5:
            print("The oracle said yes (1/4).\n")
    elif value>0.5:
        print("The oracle said no (3/4). \n")

# prove the probability is indeed 1/4
    for i in range(0,Ntrials):
        if random.random()<=0.5:
            if random.random()<=0.5:
                YES1+=1

# probability of 1/3
    onehead=False
    instance=-1
    while onehead==False:
        nohead=0
        for i in range(0,3):
            if random.random()<=0.5:
                nohead+=1
                instance=i
        if nohead==1:
            onehead=True
    if instance==0:
        print("The oracle said yes (1/3).\n")
    else:
        print("The oracle said no (2/3).\n")

# prove the probability is indeed 1/3
    for n in range(0,Ntrials):
        onehead=False
        instance=-1
        while onehead==False:
            nohead=0
            for i in range(0,3):
                if random.random()<=0.5:
                    nohead+=1
                    instance=i
            if nohead==1:
                onehead=True
        if instance==0:
            YES2+=1

    print(Ntrials, " trials were conducted. \n")
    print("for P=1/4 trials, there were ", YES1, " instances of YES. \n")
    print("for P=1/3 trials, there were ", YES2, " instances of YES. \n")










