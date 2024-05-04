nums = list(map(int, input().split(',')))
target = int(input())

flag = False
for i in range(len(nums)):
    for j in range(len(nums)):
        if i + j == target and i < j:
            print('和为目标值的两个整数的下标是 ({}, {})'.format(i, j))
            flag = True

if flag == False:
    print('和为目标值的两个整数的下标是 未找到')