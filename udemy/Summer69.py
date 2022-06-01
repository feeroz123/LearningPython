# SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9
# (every 6 will be followed by at least one 9). Return 0 for no numbers.

def summer_69(arr):
    sum = 0
    flag = True

    for i in arr:
        if i == 6:
            flag = False
        elif i == 9:
            flag = True
        elif flag:      # Checking if the flag is True (by default)
            sum += i

    print(sum)

summer_69([1, 3, 5]) #--> 9
summer_69([4, 5, 6, 7, 8, 9]) #--> 9
summer_69([2, 1, 6, 9, 11]) #--> 14