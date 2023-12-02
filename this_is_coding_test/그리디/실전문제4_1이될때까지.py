# TODO // O 한번에 푸는 방법도 익히자

# 1빼기
# k 로 나누기
# 최대한 많이 나눠야 이득.
import sys

n, k = map(int, sys.stdin.readline().split())
cnt = 0
while True:
    if n == 1:
        break
    if n % k == 0:
        n //= k
    else:
        n -= 1
    cnt += 1
print(cnt)

while True:
    target = (n // k) * k
    cnt += (n - target)
    n = target
    if n < k:
        break
    cnt += 1
    n //= k

cnt += (n - 1)
