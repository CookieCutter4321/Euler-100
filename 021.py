"""
Project Euler Problem 21
========================

Let d(n) be defined as the sum of proper divisors of n (numbers less than
n which divide evenly into n).
If d(a) = b and d(b) = a, where a =/= b, then a and b are an amicable pair
and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22,
44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1,
2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

def d(n):
    i = 2
    pairs_list = []
    while i ** 2 <= n:
        other_pair = n / i
        if n % i == 0 and i != int(other_pair):
            pairs_list.append(i)
            pairs_list.append(int(other_pair))
        i += 1
    
    res = sum(pairs_list) + 1
    return res

s = 0

seen = set()
for i in range(2,10000):
    res = d(d(i))
    if res == i and (i != d(i)) and i not in seen and res not in seen:
        seen.add(i)
        seen.add(d(i))
        s += i + d(i)
        
print(s)