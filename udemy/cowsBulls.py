# Create a program that will play the “cows and bulls” game with the user. The game works like this:
# Randomly generate a 4-digit number. Ask the user to guess a 4-digit number.
# For every digit that the user guessed correctly in the correct place, they have a “bull”.
# For every digit the user guessed correctly in the wrong place is a “cow.”
# Every time the user makes a guess, tell them how many “cows” and “bulls” they have.
# Once the user guesses the correct number, the game is over.
# Keep track of the number of guesses the user makes throughout teh game and tell the user at the end.


def splitNumbers (num):
    splitNum = num[::1]
    return splitNum

correctNum = "1098"
cows = 0
bulls = 0

userNum = str(input("Guess the 4 digit number: "))

splitCorrectNum = splitNumbers(correctNum)
print(splitCorrectNum)
splitUserNum = splitNumbers(userNum)
print(splitUserNum)

if userNum != correctNum:
    for element in splitUserNum:
        if element in splitCorrectNum:
            cows += 1
    for i in range(0, 4):
        if splitCorrectNum[i] == splitUserNum[i]:
            bulls += 1
else:
    print("You guessed it right !!")

print("You got these many Bulls: ", bulls)
print("You got these many Cows: ", cows)



