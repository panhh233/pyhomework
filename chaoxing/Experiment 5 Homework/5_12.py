def P(n, x):
    if n == 0:
        return 1
    if n == 1:
        return x
    else:
        return ((2*n-1)*x*P(n-1,x)-(n-1)*P(n-2,x))/n

n = int(input()) ; x = eval(input())
print('Legendre多项式的值： {}'.format(P(n, x)))