'''By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?'''

def isprime(n):
    for m in range(2, n):
        if n % m == 0:
            return false
    return True

def getnthprime(num):
    n = 1, factors = [], num = (10e3)+1
    while len(factors) <= num:
        n + 1
        if isprime:
            factors.append(n)
    return factors[-1]
    
print getnthprime(10001) 