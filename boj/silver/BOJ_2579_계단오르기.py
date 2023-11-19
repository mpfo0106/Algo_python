import sys
# n = int(sys.stdin.readline().strip())
#
# stair =[]
# stair.append(0)
# ans = [0]*(n+1)
# cnt = 0
# for i in range(n):
#     stair.append(int(sys.stdin.readline().strip()))
#
# ans[1]= stair[1]
# for i in range(2,n+1):
#     if cnt <2:
#         if ((ans[i-1]+stair[i]) - (ans[i-2]+stair[i])) >= 0:
#             cnt+=2
#         else:
#             cnt =0
#         ans[i] = max(ans[i-1]+stair[i], ans[i-2]+stair[i])
#     else:
#         ans[i] = ans[i-2]+stair[i]
#         cnt=0
# print(ans[n])
import sys
n = int(sys.stdin.readline().strip())
stair = [0]
for _ in range(n):
    stair.append(int(sys.stdin.readline().strip()))

ans= [0] *(n+1)
ans[1] = stair[1]
if n>1:
    ans[2] = stair[1] + stair[2]
for i in range(3,n+1):
    ans[i] = max(ans[i-2], ans[i-3]+stair[i-1])+stair[i]

print(ans[n])
