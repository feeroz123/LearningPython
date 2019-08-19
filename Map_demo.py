# Demonstrate map() function


def square(nums):
    return nums**2


my_nums = [1, 2, 3, 4, 5]

# Way 1 - Iterating over the mapped items
for i in map(square, my_nums):
    print(i)

# Way 2 - Printing list of mapped items
print(list(map(square, my_nums)))
