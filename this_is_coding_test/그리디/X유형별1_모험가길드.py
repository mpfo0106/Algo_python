# # N 명 모험가
# # 공포도가 X인 모험가는 반드시 X명 이상으로 구성
# # 1 2 2 2 3
#
# # 3을 넣는 경우 cnt
# # 2 를 넣는 경우 cnt
#
# import sys
# from collections import deque
#
# n = int(sys.stdin.readline().strip())
# p = list(map(int, sys.stdin.readline().rstrip().split()))
# p.sort(reverse=True)
# max_cnt = 0
# for i in range(n - 1):
#     cnt = 0
#     q = []
#     q = deque(p)
#     while q:
#         fear = p[i]
#         for _ in range(fear):
#             if q:
#                 q.popleft()
#             else:
#                 cnt -= 1
#                 break
#         cnt += 1
#     if max_cnt < cnt:
#         max_cnt = cnt
#
# print(max_cnt)

n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0
count = 0

for i in data:
    count += 1
    if count >= i:
        result += 1
        count = 0

print(result)
