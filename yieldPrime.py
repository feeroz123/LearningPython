
def getNextPrime(n):
    for i in range(2, n):
        for j in range(2, i):
            if i % j != 0:
                yield i


u = 'y'
num = getNextPrime(100)

while u == 'y':
    print(next(num))
    u = input("Print next Prime? y/n ")
