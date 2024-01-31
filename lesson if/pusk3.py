str1 = input()
str2 = input()
str3 = input()
if (('три' in str1 or 'три' in str2 or 'три' in str3) and ('два' in str1 or 'два' in str2 or 'два' in str3) and
   ('один' in str1 or 'один' in str2 or 'один' in str3) and ('раз' in str1 or 'раз' in str2 or 'раз' in str3)):
    print('ПУСК')
else:
    print('ОШИБКА')