maska = input()
if ('?' in maska or '*' in maska) and ' ' not in maska:
    print('Возможно маска')
else:
    print('Нет, это не маска!')
