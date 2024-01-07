# 무게가 다른 볼링공. 같은 무게 여러개 ㄱㄴ.
# 1~m 무게
# 1 2 2 3 3
# 1C1 * 4C1 + 2C1 * 3C1 + 2C1 * 3C1 =
import sys

n, m = map(int, sys.stdin.readline().split())  # 개수 n,최대 무게 m
data = list(map(int, sys.stdin.readline().split()))
data.sort()

balls = [0] * 11
result = 0
for x in data:
    balls[x] += 1

# 1~m 까지의 각 무게에 대하여 처리
for i in range(1, m + 1):
    n -= balls[i]  # A가 선택할 수 있는 (무게가 i 인 볼링공의 개수) 제외.
    result += balls[i] * n

print(result)
