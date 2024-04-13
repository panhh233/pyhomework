def series_iterative(n):
    result = 0
    for i in range(1, n + 1):
        result += i / (2 * i + 1)
    return result

def series_recursive(n):
    if n == 0:
        return 0
    else:
        return n / (2 * n + 1) + series_recursive(n - 1)

n = int(input())

print('递推法 f({})= {}'.format(n, series_iterative(n)))
print('递归法 f({})= {}'.format(n, series_recursive(n)))