def IsPrime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def IsPalindromePrime(num):
    if IsPrime(num):
        num_str = str(num)
        if num_str == num_str[::-1]:
            return True
    return False

def PalindromePrime(limit):
    prime = 2
    sequence = 0
    while sequence < limit:
        if IsPalindromePrime(prime):
            sequence += 1
            print(prime, end=',')
            if sequence % 10 == 0:
                print()
        prime += 1

x = eval(input())
PalindromePrime(x)