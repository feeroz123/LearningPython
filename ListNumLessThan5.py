# Write a program that prints out all the elements of the list that are less than 5.

count = int(input("Enter the size of your list: "))
ulist = []

for i in range (0, count):
    ulist.append(int(input("Enter value: ")))

print ("Entered list items: ", ulist)
print("Values less than 5 are: ")
print ([j for j in ulist if j < 5])

