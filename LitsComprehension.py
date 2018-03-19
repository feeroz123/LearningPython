# Write one line of Python that takes a list and makes a new list that has only the even elements of this list in it.

a = [5,10,20,17]

print([i for i in a if i%2 == 0])   # list comprehension
