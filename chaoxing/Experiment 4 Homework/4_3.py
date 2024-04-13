n=int(input())

for i in range(n+1):
    print("{}{}".format((n-i)*" ",str(i)*(2*i+1)))