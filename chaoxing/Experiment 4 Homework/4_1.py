num = int(input())

num1 = num
newnum = ''

while num != 0:
    a = num % 10
    newnum = newnum + str(a)
    num = num // 10

print('{}的反序数是:{}'.format(num1, newnum))