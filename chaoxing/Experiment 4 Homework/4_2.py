N = int(input())

K, sum = 1, 1
while sum < N:
    K += 1
    sum += K**2

print('最大K值是{}'.format(K - 1))