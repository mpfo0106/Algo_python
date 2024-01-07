# N 개의 동전을 이용해
# 만들 수 없는 양의 정수 중 최솟값

# 1. 정렬 11239
# 2. 한개 넣고

# 3. 전부 경우를 기록하기보다 1부터 위로 가면서 못만들면 끝


import sys

n = int(sys.stdin.readline())
coins = list(map(int, sys.stdin.readline().split()))
coins.sort()
target = 1
for coin in coins:
    # 만들 수 없는 금액을 찾았을때 반복 종료
    if target <coin:
        break
    target += coin
print(target)