import sys
n,m = map(int,sys.stdin.readline().split())
money = []
for _ in range(n):
    money.append(int(sys.stdin.readline()))
money.sort(reverse=True)
dp = [0] * 10000

for i in range(1,m):
    while m>0:
        if m% money[n-1] == 0:
            dp[i]= min(m//money[n-1], dp[i-money[n]] +1)
        else:
            n

    print(-1)