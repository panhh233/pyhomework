with open(r'sy8-1a.txt', 'r', encoding = 'utf-8') as f:
    with open(r'sy8-1b.txt', 'w', encoding = 'utf-8') as w:
        lst = list(map(int, f.read().split(',')))

        lst_max = max(lst)
        lst_min = min(lst)
        lst_average = sum(lst) / len(lst)

        for i in [lst_max, lst_min, lst_average]:
            w.write(str(i) + '\n')