'''
The following iterative sequence is defined for the set of positive integers:

n/2 (n is even)
3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 --> 40 -->20 -->10 -->5 -->16 -->8 -->4 -->2 -->1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''

def get_chain_length(num):
    chain_length = 0  
    while num > 1:
        if num % 2 == 0:
            num /= 2   
        else: # num % 2 != 0:
            num = num / 3 + 1
        chain_length += 1        
    return chain_length

def get_longest_chain(num):
    start_nums = range(1, num + 1)
    lengths = map(get_chain_length, start_nums)
    return sorted(zip(lengths, start_nums))[-1][-1]
             
print get_longest_chain(1000000)
        
