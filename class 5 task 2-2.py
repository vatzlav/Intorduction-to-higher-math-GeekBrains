# Class 5
# Task 2-2
# A simple program that generates 10 arrays of random numbers
# and draws histograms of their sums

import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

total_sums = []
for i in range (10):
    x = np.random.rand(10)
    total_sums.append(sum(x))
    i += 1
    
num_bs = 10
num, num_bs, patches = plt.hist(total_sums, num_bs)

plt.xlabel('Summa')
plt.ylabel('Probability')
plt.title('Histogram')
plt.show()



    
        
        
