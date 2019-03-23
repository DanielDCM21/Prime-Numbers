#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 08:14:15 2019

@author: danilo
"""
import math
def prime(x):
    contador=0
    if(x%2==0):
        contador=contador+1
    for i in range(2, x+1):
        for j in range (2,i):
            if(i%j==0):
                break;
            else:
                if(j==(i-1)):
                    contador=contador+1 
    return contador

def main():
    x=eval(input("Put in the number: "))
    n=prime(x)
    print (n)
    nprime=(n)/(x/(math.log(x)))
    print (nprime)    
main()

"""
import math
def main():
    x=eval(input("Put in x"))
    n=10
    while(n<=x):
        nprime=1*(n/math.log(n))
        
        print("n\t\t n/in(n)")
        
        print ("{0}\t\t{1:.0f}".format(n,nprime))
        
        n=n*10
main()
"""