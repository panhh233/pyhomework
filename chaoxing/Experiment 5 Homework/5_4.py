a, b = eval(input())

def coprime(x, y):
    s = x ; t = y
    while y:
        x, y = y, x % y
    if x == 1:
        print('{}和{}互质'.format(s, t))
    else:
        print('{}和{}不互质'.format(s, t))

coprime(a, b)