'''By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?'''

#def isprime(n, smallerprimes):
#    for m in smallerprimes:
#        if n % m == 0:
#            return False
#    return True

def getprimes(count):
    n = 2
    primes = []
    while len(primes) < count:
        if all(n % p > 0 for p in primes):
            primes.append(n)
        n += 1
    return primes

def getnthprime(count):
    return getprimes(count)[-1]
    
print getprimes(10001)[-1]

