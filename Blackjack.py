# BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum.
# If their sum exceeds 21 and there's an 11 in entered numbers, reduce the total sum by 10.
# Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'

def blackjack(a, b, c):
    sum = a + b + c
    if sum <= 21:
        result = sum
    elif a == 11 or b == 11 or c == 11:
        sum = sum - 10
        if sum > 21:
            result = "BUST"
        else:
            result = sum
    else:
        result = "BUST"

    print(result)


blackjack(5,6,7) #--> 18
blackjack(9,9,9) #--> 'BUST'
blackjack(9,9,11) #--> 19
blackjack(11,11,11) #--> 'BUST'
