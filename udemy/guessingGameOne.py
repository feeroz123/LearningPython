# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number,
# then tell them whether they guessed too low, too high, or exactly right.

import random

genNum = random.randint(1, 9)
unum = int(input("Guess the number : "))

if unum == genNum:
    print("Exactly Right!")
elif unum < genNum:
    print("Too Low !")
else:
    print("Too High !")

print("Number is: ", genNum)