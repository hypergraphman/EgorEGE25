text = input()
if ('вор' in text or 'Вор' in text) and 'ворон' not in text:
    print('Полиция!')
elif 'ворон' in text:
    print('Кар!')

