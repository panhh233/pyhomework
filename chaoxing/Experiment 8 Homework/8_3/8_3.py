def IsPrime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

with open(r'sy8-3.txt', 'w', encoding = 'utf-8') as file:
    prime_list = []
    for i in range(1, 101):
        if IsPrime(i):
            prime_list.append(str(i))
    content = ', '.join(prime_list)
    file.write(content)