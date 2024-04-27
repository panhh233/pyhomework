String = input()

count1 = String.count('(')
count2 = String.count(')')

if count1 == count2:
    print('配对成功')
else:
    print('配对不成功')
