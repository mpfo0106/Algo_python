import sys
n,m = map(int,sys.stdin.readline().split(" "))
card_min = [0]*n

for i in range(n):
    data = list(map(int,sys.stdin.readline().split(" ")))
    card_min[i] = min(data)
print(max(card_min))