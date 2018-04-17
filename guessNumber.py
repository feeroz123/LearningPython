# You, the user, will have in your head a number between 0 and 100.
# The program will guess a number, and you, the user, will say whether it is too high, too low, or your number.
# At the end of this exchange, your program should print out how many guesses it took to get your number

count = 0
start_val = 0
end_val = 101       # Keeping this at 100 wil never guess 100
mid_val = int((start_val+end_val)/2)

response = 0

while response != 1:
    count = count+1
    if response == 2:
        end_val = mid_val
        mid_val = int((start_val+end_val)/2)
    if response == 3:
        start_val = mid_val
        mid_val = int((start_val + end_val) / 2)

    print("Is your number => " + str(mid_val) + " ?")
    response = int(input("Enter your choice: 1 - Correct, 2 - Too High, 3 - Too Low ==> "))

print("Guessed in " + str(count) + " attempts")