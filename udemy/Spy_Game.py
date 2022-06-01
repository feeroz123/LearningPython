# SPY GAME: Write a function that takes in a list of integers and returns True if it contains 0, 0, 7 in the same consecutive order

def spy_game(nums):
    count_0 = 0
    count_7 = 0
    for i in nums:
        if i == 0:
            count_0 += 1
        if i == 7 and count_0 == 2:
            count_7 += 1

    if count_0 >= 2 and count_7 >= 1:
        print("True")
    else:
        print("False")



spy_game([1, 2, 4, 0, 0, 7, 5]) #--> True
spy_game([1, 0, 2, 4, 0, 5, 7]) #--> True
spy_game([1, 7, 2, 0, 4, 5, 0]) #--> False
spy_game([1, 0, 2, 0, 4, 5, 0]) #--> False