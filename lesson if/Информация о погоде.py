pogoda = input()
t = input()
osadki = input()
if osadki == 'нет':
    print('Cегодня', pogoda + ',', t, 'градусов, осадков нет')
if osadki == 'да':
    print('Cегодня', pogoda + ',', t, 'градусов, осадки')
