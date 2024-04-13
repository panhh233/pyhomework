from math import sqrt

a, b, c = eval(input())

if a == 0 and b == 0:
    print('方程无意义')
elif a == 0 and b != 0:
    x = -c/b
    print('方程有一个根:{:.2f}'.format(x))
else:
    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = (-b + sqrt(delta))/(2*a)
        x2 = (-b - sqrt(delta))/(2*a)
        print('方程有两个不等实根:x1={:.2f},x2={:.2f}'.format(x1, x2))
    elif delta == 0:
        x1 = x2 = -b/(2*a)
    else:
        x1 = complex(-b/(2*a), sqrt(-delta)/(2*a))
        x2 = complex(-b/(2*a), -sqrt(-delta)/(2*a))
        print('方程有两个不等虚根:x1={:.2f},x2={:.2f}'.format(x1, x2))