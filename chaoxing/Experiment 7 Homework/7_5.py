num = int(input())

start = 1
k = 2

for i in range(num):
    start += i
    row = start
    print(start, end = ' ')
    for j in range(k, num + 1):
        row += j
        print(row, end = ' ')
    print()
    k += 1