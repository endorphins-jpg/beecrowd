# Time limit exceeded

def fib(n):
    global num_calls
    num_calls += 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (fib(n-1) + fib(n-2))

runs = int(input())

for i in range(runs):
    x = int(input())
    num_calls = -1
    res = fib(x)
    print(f"fib({x}) = {num_calls} calls = {res}")