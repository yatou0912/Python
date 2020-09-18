def fib(max):
    n, a, b = 0, 0, 1
    d=[]
    while n < max:
        d.append(b)
        a, b = b, a + b
        n = n + 1
    print(d)
fib(18)
