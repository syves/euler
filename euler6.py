'''The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 102 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

def square_of_sum(n):
    return sum(range(n + 1)) ** 2

def sum_of_squares(n):
    if n == 0:
        return 0
    else:
        return n * n + sum_of_squares(n - 1)

def diff(n):
    return square_of_sum(n) - sum_of_squares(n)

print diff(100)
