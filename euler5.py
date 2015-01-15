#/*2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20? */

#def list = range(1, 21)

def factorize(num):
    for n in range(2, num):
        if num % n == 0:
            return [n] + factorize(num / n)
    return [num]

def get_counts(list_):
    counts = {}
    for item in list_:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts

def smallest_product(min_, max_):
    all_counts = {n: get_counts(factorize(n)) for n in range(min_, max_ + 1)}
    product = 1
    for n in all_counts:
        count = max(*[counts.get(n, 0) for counts in all_counts.values()])
        if count > 0:
            product *= n ** count
    return product

print(smallest_product(1, 20))

