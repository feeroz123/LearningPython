def findE(num):
    e = 1
    factr = 1
    for i in range(0,num+1):
        factr = factorial(i)
        e += 1/factr;
    return e


def factorial(num):
    fact = 1
    for k in range(1, num+1):
        fact *= k
    return fact


u = int(input("Enter the number of digits for value of e: "))

while u > 10:
    u = int(input("Can not take more tha 10. Reenter value: "))

print("Value of e is: ", findE(u))

