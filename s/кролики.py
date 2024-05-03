n = int(input())
k1 = 0
k2 = 1
count = 1
while k2 + k1 <= n:
    k1, k2 = k2, k1 + k2
    count += 1
if n == k2:
    print(count)
else:
    print('НЕТ')