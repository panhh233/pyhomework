eps=eval(input())

pi=0
n=1
t=1

while abs(t)>=eps:
    pi=pi+t
    n=n+1
    t=(-1)**(n-1)/(2*n-1)

pi=4*pi
print('近似值为:',pi,sep='')