# TODO // X
# 높이의 최대값을 구하기
# M은 충족시켜야해.
# 이진탐색으로 가운데로 짤라보고 부족하거나 남으면 계속 땡겨서

# 현재 이 높이로 자르면 조건을 만족하는가? y or n
import sys

n, m = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))

start = 0
end = max(array)

result = 0

while start <= end:
    total = 0
    mid = (start + end) // 2
    for x in array:
        if x > mid:
            total += x - mid
    if total < m:  # 부족하다면
        end = mid - 1
    else:  # 남는다면
        result = mid  # 최대한 덜잘랐을때가 정답임으로 일단 result 기록
        start = mid + 1

print(result)
