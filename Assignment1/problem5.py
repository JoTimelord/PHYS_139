#!/usr/bin/python3

import random
import os

def bridge(val):
    H1=[1,1,0,0,0]
    H2=[1,0,0,0,0]
    H3=[1,1,1,0,0]
    H4=[0,0,0,0,0]

    if val<=0.1:
        return H1
    elif val>0.1 and val<=0.4:
        return H2
    elif val>0.4 and val<=0.5:
        return H3
    else:
        return H4

if __name__=="__main__":
    # gnome=0, troll=1
    Ntrials=100000
    random.seed(a=None)
    safe=0
    captroll=0
    safe2=0

    for i in range(0,Ntrials):
        val1=random.random()
        bri=bridge(val1)
        capcreature=random.choice(bri)
        if capcreature==1:
            captroll+=1
            if sum(bri)-capcreature==0:
                safe2+=1
        if sum(bri)-capcreature==0:
            safe+=1

    print(Ntrials, " trials are conducted.")
    print(safe, " safe crossings are made.")
    print("The probability of safe crossings when one of the creatures is captured is ", safe/Ntrials)
    print("The probability of safe crossings when the captured creature is a troll is ", safe2/captroll)







