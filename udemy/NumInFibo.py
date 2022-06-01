def gen_fibo(size):
    fibo_series = []
    a = 0
    b = 1
    fibo_series.append(a)
    fibo_series.append(b)
    while len(fibo_series) <= size:
        c = a + b
        fibo_series.append(c)
        a = b
        b = c
    print("Fibonacci Series of size ", size, "  ===> ", fibo_series)
    return fibo_series


size = int(input("Enter the size of Fibonacci series to be generated: "))
num = int(input("Enter number to search in Fibonacci series: "))
if num in gen_fibo(size):
    print("---- Number was found in Fibonacci series ---")
else:
    print("*** Number was Not found in Fibonacci series ***")