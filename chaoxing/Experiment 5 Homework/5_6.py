def FacSum(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum

x = int(input())

count = 0
for num in range(1, x):
    sum1 = FacSum(num)
    sum2 = FacSum(sum1)
    if num == sum2 and num < sum1:
        print('亲密数对: A={:>4}, B={:>4}'.format(num, sum1))
        count += 1

if count == 0:
    print('输出为空')
else:
    pass