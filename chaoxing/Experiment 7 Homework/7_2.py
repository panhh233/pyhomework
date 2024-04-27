number = int(input())

inputnumber = number
seen = set()
while number != 1 and number not in seen:
    seen.add(number)
    number = sum(int(i) ** 2 for i in str(number))

flag = (number == 1) 

if flag:
    print('{}是快乐数字'.format(inputnumber))
else:
    print('{}不是快乐数字'.format(inputnumber))