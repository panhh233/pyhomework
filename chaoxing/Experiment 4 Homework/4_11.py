M, N = int(input()), int(input())

s = 0

if N % 2 == 0:
    for i in range(M + 1):
        if i * 2 + (M - i) * 4 == N:
            print('鸡有{}只，兔有{}只'.format(i, M - i))
            break
        s += 1
        if s == M:
            print('求出的只数为负，输入的数据不合理！')
else:
    print('输入的脚数为奇数，不合理！')