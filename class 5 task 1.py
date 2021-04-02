# Class 5
# Task 1
# A simulation of American roullette (random numbers 1-36 plus 2 'zeros' = total 38 numbers)

import random

def move_roulette():
    val = random.randint(1, 38)
    if val == 37 or val == 38:
        print('Zero!')
    elif val % 2 != 0 and val < 37:
        print(val, ' - Red!')
    elif val % 2 == 0 and val < 37:
        print(val, ' - Black!')

for p in range(5):
    move_roulette()

    
        
        
