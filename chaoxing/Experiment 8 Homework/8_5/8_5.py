year = int(input())

with open(r'sy8-5.csv', 'r', encoding = 'utf-8') as file:
    table = file.readlines()
    for line in table:
        if str(year) in line:
            print(line[0])