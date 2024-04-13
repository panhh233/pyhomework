M1, M2, M3 = eval(input()), eval(input()), eval(input())

average_score = (M1 + M2 + M3) / 3
if (average_score > 95) or (M1 == M2 == 100 and M3 >= 80) or (M1 == M3 == 100 and M2 >= 80) or (M2 == M3 == 100 and M1 >= 80):
    print('该同学获得一等奖学金。')
elif (average_score > 90) or (M1 == 100 and M2 >= 75 and M3 >= 75) or (M2 == 100 and M1 >= 75 and M3 >= 75) or (M3 == 100 and M1 >= 75 and M2 >= 75):
    print('该同学获得二等奖学金。')
elif M1 >= 70 and M2 >=70 and M3>=70:
    print('该同学获得三等奖学金。')
else:
    print('该同学没有获得奖学金。')