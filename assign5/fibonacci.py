def fib(n, fibs=None):
    if fibs is None: fibs={1:1, 2:1}
    if n not in fibs:
        fibs[n] = fib(n-1, fibs) + fib(n-2, fibs)
    return fibs[n]

print(fib(10))