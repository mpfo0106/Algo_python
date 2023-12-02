# TODO //X

# N개로 M 원이 되게 구성
# 순서 다르면 다름
# 최소한의 화폐개수
import sys

n, m = map(int, sys.stdin.readline().split())
array = []
for _ in range(n):
    array.append(int(sys.stdin.readline()))
d = [10001] * (m + 1)
d[0] = 0

for i in range(n):
    for j in range(array[i], m + 1):
        if d[j - array[i]] != 10001:
            d[j] = min(d[j], d[j - array[i]] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])
