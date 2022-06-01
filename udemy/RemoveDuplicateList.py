# Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

def getList(Size):
    getList = []
    for i in range(0,Size):
        getList.append(int(input("Enter value: ")))
    return getList

def remDupl(list):
    return set(list)       # set() function is used to remove duplicates from the list and store as a Set


listSize = int(input("Enter your list size: "))
genList = getList(listSize)
print("Entered list is: ", genList)
print("Unique list is: ", remDupl(genList))



