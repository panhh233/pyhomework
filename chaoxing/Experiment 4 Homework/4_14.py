x = eval(input())

s = 0
t = x
n = 1

while abs(t) >= 0.000001:
    s += t
    n += 1
    t = t*(-x*x)/((2*n-2)*(2*n-1))

print('sin({})的近似值为:{}'.format(x, s))