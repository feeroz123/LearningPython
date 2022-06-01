# Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.

import string


def up_low(s):
    count_low = 0
    count_up = 0
    count_others = 0

    for i in range(len(s)):
        if s[i] in string.ascii_lowercase:
            count_low += 1
        elif s[i] in string.ascii_uppercase:
            count_up += 1
        else:
            count_others += 1

    print("Original String :  ", s)
    print("No. of Upper case characters :  ", count_up)
    print("No. of Lower case Characters :  ", count_low)



s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)