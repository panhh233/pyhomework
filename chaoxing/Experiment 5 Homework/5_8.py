def prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

a, b = eval(input())

for r in range(a, b + 1):
    if r % 2 == 0:
        for s in range(2, r - 1):
            if prime(s) and prime(r - s):
                print('{}={}+{}'.format(r, s, r - s))
                break

#test