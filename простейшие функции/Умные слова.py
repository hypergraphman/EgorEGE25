str1 = input()
str2 = input()
str3 = input()
if str1 > str2:
    str1, str2 = str2, str1
if str2 > str3:
    str3, str2 = str2, str3
if str1 > str2:
    str1, str2 = str2, str1
print(str1)
print(str3)
print(len(str2))