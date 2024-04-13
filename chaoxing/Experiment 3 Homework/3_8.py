year = eval(input())
month = eval(input())

Dict = {1: [31, '一'], 2: [28, 29, '一'], 3: [31, '一'], 4: [30, '二'], 5: [31, '二'], 6: [30, '二'],
        7: [31, '三'], 8: [31, '三'], 9: [30, '三'],  10: [31, '四'], 11: [30, '四'], 12: [31, '四']}

if type(year) == int and 1000 <= year <= 2100 and type(month) == int and 1 <= month <= 12:
    if (year % 4 == 0 and year % 100 != 0) or year % 400 ==0:
        print('{}年是闰年'.format(year))
        if month == 2:
            print('{}月是第{}季度'.format(month, Dict[2][2]))
            print('{}月有{}天'.format(month, Dict[2][1]))
        else:
            print('{}月是第{}季度'.format(month, Dict[month][1]))
            print('{}月有{}天'.format(month, Dict[month][0]))
    else:
        print('{}年不是闰年'.format(year))
        if month == 2:
            print('{}月是第{}季度'.format(month, Dict[month][2]))
            print('{}月有{}天'.format(month, Dict[month][0]))
        else:
            print('{}月是第{}季度'.format(month, Dict[month][1]))
            print('{}月有{}天'.format(month, Dict[month][0]))
else:
    print('输入的年份或月份不合法!')