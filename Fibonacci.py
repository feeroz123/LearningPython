# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them

def getfib(num):
    a = 0
    b = 1
    print(a)
    print(b)
    for i in range (0,num-2):
        c = a + b
        print(c)
        a = b
        b = c


unum = int(input("Enter the number of elements to generate in Fibonacci series: "))
getfib(unum)
