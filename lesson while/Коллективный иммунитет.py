line = input()
count_yes = 0
count_all = 0
while line != '':
    if line == 'да':
        count_yes += 1
    count_all += 1
    line = input()
if count_yes / count_all * 100 >= 80:
    print('Достигли')
else:
    print('Пока нет')
