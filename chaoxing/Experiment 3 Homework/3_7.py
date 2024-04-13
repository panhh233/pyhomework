M, N = int(input()), int(input())

x = 2*M - N / 2
y = M - x

if N % 2 != 0:
    print('输入的脚数为奇数，不合理！')
else:
    if x < 0 or y < 0:
        print('求出的只数为负，输入的数据不合理！')
    else:
        print('鸡有{:.0f}只，兔有{:.0f}只'.format(x, y))