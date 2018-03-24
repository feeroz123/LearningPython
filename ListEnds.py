# Write a program that takes a list of numbers and makes a new list of only the first and last elements of the given list.
#  For practice, write this code inside a function.

def listends(a):
    return [a[0],a[-1]]

series = [7,2,6,7,3,4,10]

print(listends(series))