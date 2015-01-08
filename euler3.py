import math

def isprime(n):
    ceil_sqrt_n = math.ceil(math.sqrt(n))
    for x in range(2, int(ceil_sqrt_n)):
        if n % x == 0:
            return False
    return True

def factorize(n):
    """
    Returns a set of factors of n.
    """
    ceil_sqrt_n = math.ceil(math.sqrt(n))
    factors = []
    for x in range(2, int(ceil_sqrt_n)):
        if n % x == 0:
            factors.append(x)
            factors.append(n/x)
    return factors

def euler3(n):
    """
    Problem 3 - Largest prime factor
    The prime factors of 13195 are 5, 7, 13 and 29.
    What is the largest prime factor of the number 600851475143?
    """
    return max(filter(isprime, factorize(n)))

print euler3(600851475143)

