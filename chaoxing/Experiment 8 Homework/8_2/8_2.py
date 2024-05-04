with open(r'sy8-2.csv', 'r', encoding = 'GB2312') as file:
    data = file.read()
    new_data = '姓名,班级,语文,数学,英语\n' + data

with open(r'sy8-2.csv', 'w', encoding = 'GB2312') as file:
    file.write(new_data)