# Take two lists, say for example these two:
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#and write a program that returns a list that contains only the elements that are common between the lists.
#Make sure your program works on two lists of different sizes

c = [i for i in a for j in b if i == j]
print(c)

# OR

d = [k for k in a if k in b]
print(d)