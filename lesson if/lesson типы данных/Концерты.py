a = input()
b = input()
money = int(input())
if (a == 'A' and b != 'B') or (b == 'A' and a != 'B'):
    print((money - 5) // 2)
elif (a == 'B' and b != 'A') or (b == 'B' and a != 'A'):
    print((money - 3) // 2)
else:
    print('NOT TO GO')