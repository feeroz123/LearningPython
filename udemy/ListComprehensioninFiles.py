#Given two .txt files that have lists of numbers in them, find the numbers that are overlapping.
# One .txt file has a list of all prime numbers under 1000, and the other .txt file has a list of happy numbers up to 1000.

def fileToListOfInts(filename):     # A generic function to return list of integer values present in file in form of lines

    listOfValues = []

    with open(filename) as file:
        line = file.readline().strip()          # strip() is used to trim spaces, if present any with numbers in file
        while line:
            listOfValues.append(int(line))
            line = file.readline().strip()

    return listOfValues


primelist = fileToListOfInts('primeslist.txt')
happynumlist = fileToListOfInts('happynumlist.txt')

overlapNumList = [i for i in primelist if i in happynumlist]

print(overlapNumList)
