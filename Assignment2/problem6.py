#!/usr/bin/python3

import os

filename="damagedDNAdata.txt"
file=open(filename,'r')
text=file.read()

A=text.count('A')
T=text.count('T')
C=text.count('C')
G=text.count('G')

print("There are ",A," A bases.")
print("There are ",G," G bases.")
print("There are ",T," T bases.")
print("There are ",C," C bases.")
print("There are in total ",C+G+A+T," bases.")


