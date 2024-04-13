a, b, c = eval(input())

if a > 0 and b > 0 and c > 0 and a + b > c and b + c >a and a + c > b:
    if a == b == c:
        print('三角形是等边三角形')
    elif (a == b or a == c or b == c) and (a**2 + b**2 != c**2 or a**2 + c**2 != b**2 or b**2 + c**2 != a**2):
        print('三角形是等腰非直角三角形')
    elif (a == b or a == c or b == c) and (a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2):
        print('三角形是等腰直角三角形')
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print('三角形是非等腰直角三角形')
    else:
        print('三角形是普通三角形')
else:
    print('输入的三个数，不能作为三角形的边组成三角形。')