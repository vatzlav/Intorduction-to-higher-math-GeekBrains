# Class 5
# Task 3-1
# A simple program that uses Monte Carlo method to assess certain probability
# and compares it with the probability calculated by biniminal distribution

import numpy as np
# import itertools
# import math
# import sys

k, n = 0, 10000
a = np.random.randint(0, 2, n)
b = np.random.randint(0, 2, n)
c = np.random.randint(0, 2, n)
d = np.random.randint(0, 2, n)
x = a + b + c + d
for i in range(0, n):
    if x[i] == 0:
        k += 1
  
v=(0.5**k)*(0.5**(n-k))
print(a, b, c, d)
print(x)
print(k, n, k/n, v)
        
        
