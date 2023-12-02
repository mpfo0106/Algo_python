#TODO // O

# 행을 선택
# 가장 숫자가 낮은 카드를 뽑기
# 최종적으로 가장 높은 숫자의 카드를 뽑을 수 있게 전략짜기

import sys

n, m = map(int, sys.stdin.readline().split())
data = []
maxi = 0
for _ in range(n):
    line = list(map(int, sys.stdin.readline().split()))
    line.sort()
    data.append(line)
for i in range(n):
    maxi = max(maxi, data[i][0])
print(maxi)

#TODO 정렬 안하고 min으로 바로 받아도돼