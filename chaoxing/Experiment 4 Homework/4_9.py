import math

n = int(input())

num = 0

print('{}以内的自然数对有：'.format(n))

for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        N1 = i + j
        N2 = j - i
        if (math.sqrt(N1) == int(math.sqrt(N1))) and (math.sqrt(N2) == int(math.sqrt(N2))):
            print(i, j, sep=' ')
            num += 1
print('自然数对共有{}对。'.format(num))