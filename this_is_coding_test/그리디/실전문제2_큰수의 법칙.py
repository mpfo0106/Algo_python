#TODO // O

# 중복인 수는 k번까지 더할수있음
# 또 같은 수가 있어도 중복으로 보지 않음
# n 은 자연수 개수
# m은 곱해야하는 개수
# k는 limit

import sys

n, m, k = map(int, sys.stdin.readline().split())
list = list(map(int, sys.stdin.readline().split()))
list.sort()
flag = 0
ans = 0
while m > 0:
    if flag == k:
        ans += list[-2]
        flag = 0
    else:
        ans += list[-1]
        flag += 1
    m -= 1

print(ans)
#TODO 역순 정렬 할필요없이 list[-1] [-2] 로 치자