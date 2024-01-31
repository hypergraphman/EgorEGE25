prognoz = input()
if ('дожд' not in prognoz or 'Дожд' in prognoz) and ('осадки' not in prognoz or 'Осадки' not in prognoz):
    print('Зонт не нужен.')
elif ('дожд' in prognoz or 'Дожд' in prognoz) or ('осадки' in prognoz or 'Осадки' in prognoz):
    print('Возьми зонт!')