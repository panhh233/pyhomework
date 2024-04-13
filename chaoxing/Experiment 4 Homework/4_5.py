num = eval(input())

for i in range(100, num+1):
    a = i // 100
    b = i // 10 % 10
    c = i % 10
    if a**3 + b**3 + c**3 == i:
        print(i, end=' ')