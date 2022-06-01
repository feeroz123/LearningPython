
u = int(input("Enter the number of digits for PI: "))

while u > 10:
    u = int(input("Can not take value more than 10. Renter value:"))

pi = 22/7
print(round(pi, u))
