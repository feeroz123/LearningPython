# To display sum of all numbers in given input

def sum_digits(u):
    sum_nums = 0
    for i in u:
        try:
            sum_nums += int(i)      # Converting every character to INTEGER and adding to sum
        except:
            continue
    print("Sum of numbers in given input is: ", sum_nums)


u = input("Enter an input: ")
sum_digits(u)
