salary = eval(input())

if salary <= 400:
    f = salary * 0.005
elif 400 < salary <= 600:
    f = salary * 0.01
elif 600 < salary <= 800:
    f = salary * 0.015
elif 800 < salary <= 1500:
    f = salary * 0.02
elif salary >= 1500:
    f = salary * 0.03

print('工资{}，应缴党费{:.2f}元'.format(salary, f))