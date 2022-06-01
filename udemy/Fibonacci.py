# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them

def getfib(num):
    a = 0
    b = 1
    print(a)
    print(b)
    for i in range(2, num):         # It starts from 2 as two members are already printed above
        c = a + b
        print(c)
        a = b
        b = c


unum = int(input("Enter the number of elements to generate in Fibonacci series: "))
getfib(unum)
