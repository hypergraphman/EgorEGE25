mx = -100000
mx2 = -100000
n = int(input())
while abs(n) < 1000:
    if n > mx:
        mx2 = mx
        mx = n
    elif n < mx and n > mx2:
        mx2 = n
    n = int(input())

print(mx2)
