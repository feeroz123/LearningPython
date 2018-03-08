# Python function that takes a sequence of numbers and determines if all the numbers are different from each other

def checknumbers(data):
    print(data)
    for i in data:
        count = 0
        for j in range(0, len(data)):
            if i == data[j]:
                count += 1
            if count == 2:
                return "Duplicate"

    return "Unique"


print(checknumbers([2, 8, 3, 7]))
print(checknumbers([2, 8, 8, 7]))
