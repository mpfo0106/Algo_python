import sys
n,m =map(int,sys.stdin.readline().split(" "))
num = [0] + list(map(int, sys.stdin.readline().split()))
dp = [0]*(n+1)
for i in range(1,n+1):
    dp[i] = num[i]+ dp[i-1]
for _ in range(m):
    start,end = map(int,sys.stdin.readline().split(" "))
    print(dp[end] - dp[start-1])