a = eval(input())

def x(i, j):
    if i == 0:
        return j
    else:
        return (x(i-1, j) + (j / x(i-1, j)))/2

n = 0
e = x(n, a) - x(n+1, a)

while e >= 0.000001:
    n += 1
    e = x(n, a) - x(n+1, a)

print('x的近似值为:{:.6f}'.format(x(n+1, a)))