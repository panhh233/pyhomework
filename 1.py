def f(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n == 3:
        return 1
    else:
        return f(n-1) + f(n-2) + f(n-3)

print(f(10))