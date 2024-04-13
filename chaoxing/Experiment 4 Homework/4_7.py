num = eval(input())

for i in range(1, num + 1):
    if str(i ** 2).endswith(str(i)):
        print(i)