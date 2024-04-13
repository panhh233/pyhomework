x = int(input())

if x % 2 == 1:
    y = x ** (1 / 3)
else:
    y = x ** (1 / 2)

print('y的值为:{}'.format(y))