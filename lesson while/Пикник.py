n = int(input())
k = 1
while k != n:
    if n % k == 0:
        print(k)
    k += 1
print(k)