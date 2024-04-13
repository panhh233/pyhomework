def f(num):
    if num == 1:
        return 1
    if num == 2:
        return 2
    if num == 3:
        return 3
    if num > 3:
        return f(num - 1) + f(num - 2) + f(num - 3)

M = int(input())

n = 1

while f(n) <= M:
    n += 1

print('数列从第{}项开始，数值超过{}。'.format(n, M))
print('第{}项的值为{}。'.format(n, f(n)))