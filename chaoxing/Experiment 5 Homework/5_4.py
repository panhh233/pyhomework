a, b = eval(input())

def coprime(x, y):
    s = x ; t = y
    while y:
        x, y = y, x % y
    if x == 1:
        return '{}和{}互质'.format(s, t)
    else:
        return '{}和{}不互质'.format(s, t)

print(coprime(a, b))