# Int -> (Int,Int,Int)?
def find_pythagorean_triple(sum_):
    for a in range(1, sum_ / 3):
        for b in range(a + 1, sum_ / 2):
            c = sum_ - a - b
            if a * a + b * b == c * c:
                return a, b, c
 
 
triple = find_pythagorean_triple(1000)
if triple is None:
    print('No Pythagorean triple for 30')
else:
    a, b, c = triple
    print('Product of Pythagorean triple {}, {}, {} is {}'.format(a, b, c, a * b * c))