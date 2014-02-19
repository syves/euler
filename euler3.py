#!/usr/bin/env python
# Problem 3 - Largest prime factor
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
 
import math
 
def prime(n):
    # print "In prime with %s" % n
    # sqrt_n = math.sqrt(n)
    # ceil_sqrt_n = math.ceil(sqrt_n)
    #print "Ceil... %s" % ceil_sqrt_n
    for x in range(2, n + 1):
        
        if n % x == 0:
            return False
    return True
 
 
n = 24
sqrt_n = math.sqrt(n)
ceil_sqrt_n = math.ceil(sqrt_n)
 
for x in range(2, int(ceil_sqrt_n) + 1):
    if n % x == 0 and prime(x):
        print x
        pass