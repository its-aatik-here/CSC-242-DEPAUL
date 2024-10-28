def fibonacci(n):
    x, y = 1, 1
    i = 1
    while i < n:
        x, y = y, x+y
        i = i+1
    return y

fib = {0:1, 1:1}
def fibDP(n):
    global fib
    try:
        return fib[n-1] + fib[n-2]
    except:
        if n-2 in fib:
            fib[n-1] = fib[n-2] + fib[n-3]
            return fib[n-1] + fib[n-2]
        else:
            fib[n-2] = fibDP(n-2)
            fib[n-1] = fibDP(n-1)
            return fib[n-2] + fib[n-1]

