# Demonstra Lambda function

# A lambda() function is a simple anonymous function that has one time use
# It can be demonstrated by making use of map() and filter() functions

mult_five = lambda i: i*5       # A simple lambda function that takes i and returns i*5 value. Not used like this though.
print(mult_five(3))             # Simple use of lambda function

my_nums = [1,2,3,4,5]

print("---------- Using map() with lambda() ---------------")
print(list(map(lambda num: num ** 2, my_nums)))

print("---------- Using filter() with lambda() ---------------")
print(list(filter(lambda num: num % 2 == 0, my_nums)))
