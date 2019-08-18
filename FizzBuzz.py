# 1) Generate a range of numbers from 0 to 500.
# 2) Iterate over the list and:
#   a) print "Fizz" if the number is divisible 3
#   b) print "Buzz" if the number is divisible by 5
#   c) print "FizzBuzz" if the number is divisible by 15

num_list = range(50)
for num in num_list:
    if num % 15 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
