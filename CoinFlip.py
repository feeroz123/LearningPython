# Coin Flip Simulation -
## Write some code that simulates flipping a single coin however many times the user decides.
## The code should record the outcomes and count the number of tails and heads.

import random

def flip():
    flip_value = random.randint(0, 1)
    return flip_value

uinput = 'y'
count_heads = 0
count_tails = 0

while uinput == 'y':
    print("Flipping the coin ...")
    flip_result = flip()

    if flip_result == 0:
        print("HEADS !")
        count_heads += 1
    else:
        print("TAILS !")
        count_tails += 1

    uinput = input("Flip Coin? y/n : ")

print("Game Over. Total HEADS = {} , Total TAILS = {}".format(count_heads,count_tails))
