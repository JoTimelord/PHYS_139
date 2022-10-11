#!/usr/bin/python3

import random
import argparse
import os

allh=0
allt=0
twoh=0
twot=0

def count():
    global allh
    global allt
    global twoh
    global twot
    head=0
    # First coin
    if random.random()<=0.35:
        head+=1
    # Second coin
    if random.random()<=0.65:
        head+=1
    # Third coin
    if random.random()<=0.40:
        head+=1
    # switch case
    if head==0:
        allt+=1
    elif head==1:
        twot+=1
    elif head==2:
        twoh+=1
    elif head==3:
        allh+=1
    else:
        print ("I should never be here.")

if __name__=="__main__":
# Initialize argparser
    parser=argparse.ArgumentParser()
    parser.add_argument("-n", "--trials", help="number of trials for the experiment", default=100)
    args=parser.parse_args()
    Ntrials=int(args.trials)

    random.seed(a=None)
    current=0
    while current<Ntrials:
        count()
        current+=1

    # open a file for writing the result
    result=open('result.txt', 'w')
    result.write('Trial No          P(3H)       P(3T)       P(2H1T)         P(1H2T) \n')
    result.write("%s    %s      %s      %s      %s \n"%(Ntrials, allh/Ntrials, allt/Ntrials, twoh/Ntrials, twot/Ntrials))

    # Increase the number of trials by n
    for n in range(2,20):
        while current<Ntrials*n:
            count()
            current+=1
        result.write("%s    %s      %s      %s      %s \n"%(Ntrials*n, allh/(n*Ntrials), allt/(n*Ntrials), twoh/(n*Ntrials), twot/(n*Ntrials)))

    # close file
    result.close()





