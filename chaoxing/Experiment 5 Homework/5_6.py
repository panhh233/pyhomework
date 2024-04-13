x = int(input())

def FacSum(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum

pairs = set()

for num in range(1, x):
    sum1 = FacSum(num)
    sum2 = FacSum(sum1)
    if num == sum2 and num != sum1:
        pair = ((min(num, sum1), max(num, sum1)))
        pairs.add(pair)

pairs_list = list(pairs)
pairs_list.sort()

if pairs:
    for pair in pairs_list:
        print('亲密数对: A={:>4}, B={:>4}'.format(pair[0], pair[1]))
else:
    print('输出为空')