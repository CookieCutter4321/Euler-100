"""
Project Euler Problem 20
========================

n! means n * (n - 1) * ... * 3 * 2 * 1

Find the sum of the digits in the number 100!
"""
import math

res = sum([int(c) for c in str(math.factorial(100))])

print(res)