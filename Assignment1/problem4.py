#!/usr/bin/python3

import random
import argparse
import os

def Monty(prize,initchoice):
    dupsequence=[1,2,3]
    dupsequence.remove(prize)
    if prize==initchoice:
        Montychoice=random.choice(dupsequence)
        return Montychoice
    else:
        Montychoice=sum(dupsequence)-initchoice
        return Montychoice

if __name__=="__main__":
    random.seed(a=None)

    wininit=0
    winchange=0

    Ntrials=10000
    for i in range(0,Ntrials):
        sequence=[1,2,3]
        prize=random.choice(sequence)
        initchoice=random.choice(sequence)
        Mchoice=Monty(prize,initchoice)
        if initchoice==prize:
            wininit+=1
        secchoice=6-Mchoice-initchoice
        if secchoice==prize:
            winchange+=1
    print(Ntrials," trials are conducted.")
    print("The probability of winning the prize while sticking to the initial choice is ", wininit/Ntrials)
    print("The probability of winning the prize after changing the choice is ", winchange/Ntrials)




