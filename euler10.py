'''The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.'''

import operator

def isprime(num):
    for n in range(2, num):
        if num % n == 0:
            return False
    return True
    
'''def factorize(num):
    for n in range(2, num):
        if num % n == 0:
            return [n] + factorize(num / n)
    return [num]
print factorize(49)'''


def sumprimes(num):
    return reduce(operator.__add__ ,filter(isprime, range(2, (num) + 1)))


print sumprimes(2000)


