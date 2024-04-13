a = int(input())

def Odd(x):
    if x % 2 == 0:
        return False
    else:
        return True

if Odd(a) == False:
    print('{}是偶数'.format(a))
else:
    print('{}是奇数'.format(a))