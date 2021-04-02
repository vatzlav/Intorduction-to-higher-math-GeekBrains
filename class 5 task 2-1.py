# Class 5
# Task 2-1
# A simulation of flipping 5 heads in 5 tosses
# We are going to use this simple program to check if P(AB) = P(A) * P(B).
# P(A) and P(B) are independent events
# Odds of flipping 5 heads in a row = 1/2 * 1/2 * 1/2 * 1/2 * 1/2 = 1/32 = 31,2% 

import random 

flips = 1 
heads = 0 
tails= 0 

num_tests = 10000
passed_tests = 0 


for flips in range(num_tests):
    heads, tails = 0, 0
    for subflip in range(5):
        coin = random.randint(1,2)
        if coin == 1:
            # print("Heads")
            heads += 1
        elif coin == 2:
            # print("tails")
            tails += 1
    if heads == 5:
        # print("had 5 heads in a row!")
        passed_tests+=1 

print("Got 5 heads in a row {} times {:.2%} of the time".format(passed_tests, passed_tests/float(num_tests)))


    

    
        
        
