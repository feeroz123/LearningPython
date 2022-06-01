# Implement a function that takes as input three variables, and returns the largest of the three.

def maxofthree(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c


max_val = maxofthree(12,7,9)
print("Maximum is: ", max_val)