# Create a program that asks the user to enter their name and their age.
# #Print out a message addressed to them that tells them the year that they will turn 100 years old.

import datetime
name = input("Enter your name: ")
age = int(input("Enter your age: "))

yr = int(datetime.datetime.today().strftime("%Y"))
newyr = (100 - age) + yr

print("Hello", name, ", you will turn 100 yrs old in the year", newyr)