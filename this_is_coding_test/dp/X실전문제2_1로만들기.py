# TODO //X

# 연산 4개로 최소
# 1.  X%5 ==0 -> X//=5
# 2. X%3 == 0 -> x//=3
# 3. x%2==0 -> x//=2
# 4. x-=1

x = int(input())
dp = [0] * 30001

for i in range(2, x + 1):
    dp[i] = dp[i - 1] + 1
    if i % 2 == 0:
        dp[i] = min((dp[i], dp[i // 2] + 1))
    if i % 3 == 0:
        dp[i] = min((dp[i], dp[i // 3] + 1))
    if i % 5 == 0:
        dp[i] = min((dp[i], dp[i // 5] + 1))
print(dp[x])