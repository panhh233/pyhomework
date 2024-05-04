import random

radint_list = [random.randint(0, 100) for i in range(20)]

with open(r'sy8-4.csv', 'w', encoding = 'utf-8') as file:
    line_number = []
    for j in range(len(radint_list)):
        if (j + 1) % 5 != 0:
            line_number.append(str(radint_list[j]))
        else:
            line_number.append(str(radint_list[j]))
            line = ','.join(line_number)
            file.write(line + '\n')
            line_number = []