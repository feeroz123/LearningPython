#Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) and another number.
# The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.

def search (inputList, searchValue):
        startIndex = 0
        endIndex = len(inputList)-1
        while True:
            midIndex = int((startIndex+endIndex)/2)
            midValue = inputList[midIndex]

            if midValue == searchValue or inputList[startIndex] == searchValue or inputList[endIndex] == searchValue:
                return True
                break
            if midValue == 0 or midValue == startIndex or midValue == endIndex:
                return False
                break
            elif midValue > searchValue:
                endIndex == midIndex
            else:
                startIndex = midIndex


ourList = [1,2,4,6,9,12,16]

userInput = int(input("Enter a number to search: "))

if search(ourList, userInput):
    print("Found")
else: print("Not Found")