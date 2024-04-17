word = input()
k = 0
while ' ' not in word:
    n = int(input())
    if n == len(word):
        k += 1
    word = input()
print(k)