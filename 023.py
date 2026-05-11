"""
Project Euler Problem 23
========================

A perfect number is a number for which the sum of its proper divisors is
exactly equal to the number. For example, the sum of the proper divisors
of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect
number.

A number whose proper divisors are less than the number is called
deficient and a number whose proper divisors exceed the number is called
abundant.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the
smallest number that can be written as the sum of two abundant numbers is
24. By mathematical analysis, it can be shown that all integers greater
than 28123 can be written as the sum of two abundant numbers. However,
this upper limit cannot be reduced any further by analysis even though it
is known that the greatest number that cannot be expressed as the sum of
two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the
sum of two abundant numbers.
"""

# return sum of proper divisors
def d(n):
    i = 2
    res = 1 # counting 1 initially
    while i ** 2 <= n:
        if n % i == 0:
            if n // i == i: #dont double count perfect squares
                res += i
            else:
                res += i + int(n / i)

        i += 1

    return res

def is_deficient(n):
    n_sum = d(n)

    if n_sum < n:
        return 1 # deficient
    elif n_sum > n:
        return 0 # abundant
    else:
        return -1 # perfect


abundants = [] # cross product with itself to give us a list of integers which can be formed as a sum of two abundants
for i in range(2,28124): # 28124
    check = is_deficient(i)
    if check == 0:
        abundants.append(i)

lookup = set()
for i in range(len(abundants)):
    for j in range(len(abundants)):
        lookup.add(abundants[i] + abundants[j])

lookup = sorted(list(lookup))

res = 0
for i in range(1,28124):
    if i not in lookup:
        res += i

print(res)