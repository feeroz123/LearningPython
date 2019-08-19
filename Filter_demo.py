# Demonstrate filter() function
# Filter() functions works for a given method that returns True or False to filter out results


def get_even(num):
    return num % 2 == 0

my_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Way 1 - Apply the filter function on the given list of numbers, and iterate over the results
for i in filter(get_even, my_nums):
    print(i)

# Way 2 - Get the filtered items in list and print them
print(list(filter(get_even, my_nums)))
