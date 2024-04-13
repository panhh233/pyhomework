w = eval(input())

if w <= 50:
    y = w * 0.25
else:
    y = 50 * 0.25 + (w - 50) * 0.35

print('行李的托运费是:{}元'.format(y))