n1 = int(input())
n2 = int(input())
n3 = int(input())
k = 0
while n3 != -1:
    if n1 < n2 > n3:
        k += 1
    n1 = n2
    n2 = n3
    n3 = int(input())
print(k)