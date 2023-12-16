def fib(number):
    n1 = 0
    n2 = 1
    for i in range(number):
        yield n1
        temp = n1
        n1 = n2
        n2 = temp + n2


for x in fib(10000):
    print(x)