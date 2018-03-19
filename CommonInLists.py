# Program that returns a list that contains only the elements that are common between the lists (without duplicates).
# Make sure your program works on two lists of different sizes.

import random

a = [2, 8, 1, 0, 9]
b = [4, 9, 1, 7, 0,10,13,17]
c = []

for i in a:
    if i in b:
        c.append(i)
print(c)
