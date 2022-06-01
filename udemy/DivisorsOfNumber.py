# Program that asks the user for a number and then prints out a list of all the divisors of that number

unum = int(input("Enter a number: "))

for i in range (2, int(unum/2)+1):
    if unum % i == 0:
        print ("Divisor is: " , i)
