prev = int(input())
cur = int(input())
k = 0
while cur != 0:
    if prev > cur:
        k += 1
    prev = cur
    cur = int(input())
print(k)
