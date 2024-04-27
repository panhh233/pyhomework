nums = tuple(map(int, input().split(',')))
target = int(input())

flag = False
nums = list(nums)
for i in nums:
    for j in nums:
        if i + j == target and nums.index(i) < nums.index(j):
            print('和为目标值的两个整数的下标是 ({}, {})'.format(nums.index(i), nums.index(j)))
            flag = True

if flag == False:
    print('和为目标值的两个整数的下标是 未找到')