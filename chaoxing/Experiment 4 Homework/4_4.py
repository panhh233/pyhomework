a, b, c = eval(input())

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def gcd_three(x, y, z):
    return gcd(gcd(x, y), z)

def lcm(x, y):
    return x * y // gcd(x, y)

def lcm_three(x, y, z):
    return lcm(lcm(x, y), z)

print('最大公约数是{}，最小公倍数是{}。'.format(gcd_three(a, b, c), lcm_three(a, b, c)))