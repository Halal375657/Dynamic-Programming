#Bottom-up

# input: 10
# output: 55

def fibo(n):
    fib = {}
    for k in range(1, n+1):
        if k <= 2: f = 1
        else: f = fib[k-1] + fib[k-2]
        fib[k] = f
    return fib[n]


n = 10
res = fibo(n)
print(res)
