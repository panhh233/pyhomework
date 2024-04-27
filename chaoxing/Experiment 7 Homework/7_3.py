m = int(input())
n = int(input())
k = int(input())

people = [i for i in range(1, m + 1)]
count = 0
index = 0
while count <= n:
    index = (index + k - 1) % len(people)
    print('{}号下船了'.format(people[index]))
    people.remove(people[index])
    count += 1