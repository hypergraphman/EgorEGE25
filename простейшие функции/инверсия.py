x = float(input())
if abs(x) < 10 ** -9:
    print('INFINITELY LARGE')
elif abs(x) > 10 ** 9:
    print('INFINITELY SMALL')
else:
    print(1 / x)
