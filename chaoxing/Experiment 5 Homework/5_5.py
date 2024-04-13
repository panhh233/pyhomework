m = int(input())

def fib(n):
    if n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    else:
        fib_list = [1, 1]
        for i in range(2, n):
            fib_list.append(fib_list[-1] + fib_list[-2])
        return fib_list

print(fib(m))