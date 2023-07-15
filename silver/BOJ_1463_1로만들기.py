# n = int(input())
# cnt = 0
# while(n!=1):
#     if n < 4:
#         cnt += 1
#         break
#     tmp = n % 3
#     if n%6 ==0:
#         n/=6
#         cnt+=1
#     elif tmp == 0:
#         n/=3
#     elif tmp ==1:
#         n-=1
#     else:
#         if n%2 ==0:
#             n/=2
#         else:
#             n-=1
#     cnt+=1
#
# print(cnt)
n = int(input())
ans = [0]*(n+1) #n+1로 그냥
ans[1]=0
for i in range(2,n+1):
    ans[i] = ans[i-1]+1
    if i %2 ==0:
        ans[i] = min(ans[i],ans[i//2]+1)
    if i%3 ==0:
        ans[i] = min(ans[i],ans[i//3]+1)

print(ans[n])