m = int(input())

def fib(n):
    lst = [1] * n
    if n >= 3:
        for i in range(2, n):
            lst[i] = lst[i - 1] + lst[i - 2]
    return lst

print(fib(m))