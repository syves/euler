'''
The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
'''
def get_factors(num):
    factors = [1]
    for n in range(2, num + 1):
        if num % n == 0:
            factors.append(n)
    return factors

def get_num_factors(num):
    num_factors = 0
    for n in range(1, int(num ** 0.5) + 1):
        if num % n == 0:
            num_factors += 2

    if int(num ** 0.5) ** 2 == num:
        return num_factors + 1
    else:
        return num_factors
            
#print get_factors(28)  

def trinums():
    delta = 1 #diff
    num = 1 
    while True:
        yield num
        delta += 1
        num += delta

def five_hundred_divisors(n):
    for num in trinums():
        if get_num_factors(num) > n:
            return num
            
print five_hundred_divisors(500)

            

